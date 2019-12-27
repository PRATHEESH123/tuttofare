from rest_framework import serializers

from ..models import CartItem


class CartItemSerailizer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = (
            'user',
            'product',
            'quantity',
        )
