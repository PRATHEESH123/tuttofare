from django.db.models import F

from rest_framework import serializers

from ..models import Cart

from products.serializers import ProductSerializer
from products.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = (
            'id',
            'product',
            'quantity',
        )


class CartItemAddSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = (
            'user',
            'product',
            'quantity',
        )

    def validate(self, data):
        """
        Check if the quantity is greater than stock
        """
        user = data.get('user')
        quantity = data.get('quantity')
        product = data.get('product')

        try:
            Kart = product.cart.get(user=user)
            quantity += Kart.quantity
        except Cart.DoesNotExist:
            pass

        if quantity > product.stock:
            raise serializers.ValidationError(f'only {product.stock - quantity} of {product.name} left in stock')
        return data

    def create(self, validated_data):
        quantity = validated_data.pop('quantity', None)
        instance, created = Cart.objects.get_or_create(**validated_data,)

        if not created:
            instance.quantity += quantity
            instance.save()

        return instance