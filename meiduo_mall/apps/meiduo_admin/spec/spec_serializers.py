from rest_framework import serializers
from goods.models import SPUSpecification


class Specserializers(serializers.ModelSerializer):

    spu = serializers.CharField(read_only=True)
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = "__all__"
