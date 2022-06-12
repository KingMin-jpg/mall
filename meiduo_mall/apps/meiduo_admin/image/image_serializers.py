from rest_framework.serializers import ModelSerializer
from goods.models import SKUImage, SKU


class ImageSerializer(ModelSerializer):
    class Meta:
        model = SKUImage
        fields = "__all__"

class SKUImpleSerializers(ModelSerializer):
    class Meta:
        model = SKU
        fields = ['id', 'name']
