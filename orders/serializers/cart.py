from rest_framework import serializers

from ..models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CartItem
        fields = (
            'user',
            'product',
            'quantity',
        )
