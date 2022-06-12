from rest_framework import serializers
from users.models import User


# 1, 用户序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "mobile", "email", "password"]

        extra_kwargs = {
            "password": {
                'write_only': True
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
