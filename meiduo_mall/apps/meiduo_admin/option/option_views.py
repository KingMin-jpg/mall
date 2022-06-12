from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from meiduo_admin.my_pagination import MyPageNumberPagination
from . import option_serializers
from goods.models import SpecificationOption, SPUSpecification


class OptionModelViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = option_serializers.OptionSerializer
    queryset = SpecificationOption.objects.all()


class SpecSimpleView(ListAPIView):
    pagination_class = None
    serializer_class = option_serializers.SpecSimpleSerializer
    # queryset = SPUSpecification.objects.all()

    def get_queryset(self):
        queryset = SPUSpecification.objects.all()

        for spec in queryset:
            spec.name = f"{spec.spu.name} - {spec.name}"

        return queryset
