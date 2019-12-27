# 3rd party
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

# local
from .models import User


class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'auth_token',
        )
        read_only_fields = ('auth_token',)
