from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from meiduo_admin.my_pagination import MyPageNumberPagination
from . import spu_serializers
from goods.models import SPU, Brand, GoodsCategory
from rest_framework.generics import ListAPIView
from fdfs_client.client import get_tracker_conf, Fdfs_client
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


# spu管理
class SPUModelViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = spu_serializers.SPUSerializers
    queryset = SPU.objects.all()


class GoodBrandSimpleView(ListAPIView):
    pagination_class = None
    serializer_class = spu_serializers.GoodsBrandSerializers
    queryset = Brand.objects.all()


class GoodCategorySimpleView(ListAPIView):
    pagination_class = None
    serializer_class = spu_serializers.GoodsCategorySerializers
    queryset = GoodsCategory.objects.filter(parent=None)


class GoodCategorySimpleTwoThreeView(ListAPIView):
    pagination_class = None
    serializer_class = spu_serializers.GoodsCategorySerializers

    def get_queryset(self):
        parent_id = self.kwargs.get("parent_id")
        return GoodsCategory.objects.filter(parent_id=parent_id)


# 4, spu 图片上传
class GoodsImagesView(APIView):
    def post(self, request):

        # 1,获取参数
        image = request.FILES.get("image")

        # 2,校验参数
        if not image:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 3,上传图片
        client = Fdfs_client(get_tracker_conf(settings.FDFS_CONFIG))

        # 上传
        result = client.upload_by_buffer(image.read())

        # 判断是否上传成功
        if result["Status"] != "Upload successed.":
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 获取图片名称
        image_name = result["Remote file_id"]

        # 5,拼接数据,返回响应
        img_url = "{}{}".format(settings.BASE_URL, image_name.decode())
        return Response({"img_url": img_url})
