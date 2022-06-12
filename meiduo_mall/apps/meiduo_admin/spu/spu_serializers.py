from rest_framework import serializers
from goods.models import SPU, Brand, GoodsCategory


# spu序列化器
class SPUSerializers(serializers.ModelSerializer):
    # 重写brand brand_id
    brand = serializers.CharField(read_only=True)
    brand_id = serializers.IntegerField()

    # 重写一级，二级，三级分类重写
    category1 = serializers.CharField(read_only=True)
    category1_id = serializers.IntegerField()

    category2 = serializers.CharField(read_only=True)
    category2_id = serializers.IntegerField()

    category3 = serializers.CharField(read_only=True)
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        fields = "__all__"


class GoodsBrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class GoodsCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']
