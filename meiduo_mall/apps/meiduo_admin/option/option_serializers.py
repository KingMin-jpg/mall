from rest_framework import serializers
from goods.models import SpecificationOption, SPUSpecification


class OptionSerializer(serializers.ModelSerializer):

    spec = serializers.CharField(read_only=True)
    spec_id = serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = "__all__"


class SpecSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPUSpecification
        fields = ["id", "name"]