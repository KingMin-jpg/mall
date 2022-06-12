from meiduo_admin.my_pagination import MyPageNumberPagination
from . import order_serializers
from orders.models import OrderInfo
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


class OrderModelViewSet(ReadOnlyModelViewSet):
    pagination_class = MyPageNumberPagination

    # serializer_class = order_serializers.OrderSerializer
    # queryset = OrderInfo.objects.all()

    def get_queryset(self):
        keyword = self.request.query_params.get("keyword")

        if keyword:
            return OrderInfo.objects.filter(order_id__contains=keyword).all()
        else:
            return OrderInfo.objects.all()

    # 重写get_serializer_class，判断请求方式action，不同的action返回不同的序列化器
    def get_serializer_class(self):
        # print("self.action = {}".format(self.action))

        if self.action == 'list':
            return order_serializers.OrderSerializer
        else:
            return order_serializers.OrderRetrieveSerializer

    @action(methods=['put'], detail=True)  #detail=True  会生成：order(路由前缀)/pk(路由参数)/status(方法名)
    def status(self, request, *args, **kwargs):
        a = 1
        status1 = request.data.get("status")
        order = self.get_object()

        if not status:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        order.status = status1
        order.save()

        return Response(status=status.HTTP_200_OK)
