from rest_framework.generics import ListAPIView, CreateAPIView
from users.models import User
from . import user_serializers
from meiduo_admin.my_pagination import MyPageNumberPagination


# 1, 获取用户视图
class UserView(ListAPIView, CreateAPIView):
    pagination_class = MyPageNumberPagination
    serializer_class = user_serializers.UserSerializer
    # queryset = User.objects.filter(is_staff=False).all()

    # 重写get_queryset方法，提供数据
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')

        if keyword:
            return User.objects.filter(is_staff=False, username__contains=keyword).all()
        else:
            return User.objects.filter(is_staff=False).all()
