from rest_framework.viewsets import ModelViewSet
from meiduo_admin.my_pagination import MyPageNumberPagination
from . import spec_serializers
from goods.models import SPUSpecification


class SpecModelViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = spec_serializers.Specserializers
    queryset = SPUSpecification.objects.all()


