from rest_framework import serializers
from orders.models import OrderInfo, OrderGoods
from goods.models import SKU


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OrderInfo
        fields = "__all__"


class SKUSerializers(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__'


class OrderGoodsSerializers(serializers.ModelSerializer):

    sku = SKUSerializers(read_only=True)

    class Meta:
        model = OrderGoods
        fields = ['sku', 'price', 'count']


class OrderRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    skus = OrderGoodsSerializers(read_only=True, many=True)

    class Meta:
        model = OrderInfo
        fields = "__all__"
