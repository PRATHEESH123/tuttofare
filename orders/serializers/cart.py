from rest_framework import serializers

from ..models import Cart

from products.serializers import ProductSerializer

from .items import ItemSerializer


class CartItemSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('items',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)
        return representation.pop('items')


class CartItemAddSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = (
            'user',
            'items',
        )
