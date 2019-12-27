from rest_framework import serializers

from ..models import CartItem

from products.serializers import ProductSerializer
from products.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = (
            'id',
            'product',
            'quantity',
        )


class CartItemAddSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CartItem
        fields = (
            'user',
            'product',
            'quantity',
        )
