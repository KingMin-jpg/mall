from rest_framework.viewsets import ModelViewSet
from meiduo_admin.my_pagination import MyPageNumberPagination
from . import sku_serializers
from goods.models import SKU, GoodsCategory, SPU, SPUSpecification
from rest_framework.generics import ListAPIView


# sku管理
class SKUModelViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = sku_serializers.SKUSerializers

    # queryset = SKU.objects.all()

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')

        if keyword:
            return SKU.objects.filter(name__contains=keyword)
        else:
            return SKU.objects.all()


class SKUCategoryView(ListAPIView):
    pagination_class = None
    serializer_class = sku_serializers.SKUCategorySerializers
    queryset = GoodsCategory.objects.filter(subs=None)


# 3, sku,spu
class GoodSimpleView(ListAPIView):
    pagination_class = None
    serializer_class = sku_serializers.GoodSimpleSerializer
    queryset = SPU.objects.all()


class GoodSpecsView(ListAPIView):
    pagination_class = None
    serializer_class = sku_serializers.GoodSpecsSerializer
    # queryset = SPUSpecification.objects.all()

    def get_queryset(self):
        spu_id = self.kwargs.get("spu_id")

        return SPUSpecification.objects.filter(spu_id=spu_id).all()