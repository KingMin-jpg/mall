from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from . import image_serializers
from meiduo_admin.my_pagination import MyPageNumberPagination
from goods.models import SKUImage, SKU
from rest_framework.response import Response
from rest_framework import status
from fdfs_client.client import Fdfs_client, get_tracker_conf
from django.conf import settings


class ImageModelViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = image_serializers.ImageSerializer
    queryset = SKUImage.objects.all()

    def create(self, request, *args, **kwargs):
        # 获取参数
        dict_data = request.data
        sku = dict_data.get('sku')
        image = dict_data.get('image')

        # 校验参数
        if not all([sku, image]):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 创建fdfs对象，上传
        client = Fdfs_client(get_tracker_conf(settings.FDFS_CONFIG))
        result = client.upload_by_buffer(image.read())

        # 判断是否上传成功
        if result["Status"] != "Upload successed.":
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 获取图片名称
        image_name = result["Remote file_id"]

        try:
            # 数据入库
            SKUImage.objects.create(sku_id=sku, image=image_name.decode())
            SKU.objects.filter(id=sku, default_image_url='').update(default_image_url=image_name.decode())
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # 返回响应
        return Response(status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # 获取参数
        dict_data = request.data
        sku = dict_data.get('sku')  # 需要修改的sku_id
        image = dict_data.get('image')  # 传入进来的新图片
        sku_image = self.get_object()  # 根据pk获取sku_image对象

        # 校验参数
        if not all([sku, image, sku_image]):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 创建fdfs对象，上传
        client = Fdfs_client(get_tracker_conf(settings.FDFS_CONFIG))
        result = client.upload_by_buffer(image.read())

        # 判断是否上传成功
        if result["Status"] != "Upload successed.":
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 获取图片名称
        image_name = result["Remote file_id"]

        try:
            # 数据入库
            SKUImage.objects.filter(id=sku_image.id).update(sku_id=sku, image=image_name.decode())
            SKU.objects.filter(id=sku, default_image_url=sku_image.image).update(default_image_url=image_name.decode())
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # 返回响应
        return Response(status=status.HTTP_201_CREATED)


class SKUSimpleView(ListAPIView):
    pagination_class = None
    serializer_class = image_serializers.SKUImpleSerializers
    queryset = SKU.objects.all()
