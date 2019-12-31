from rest_framework import serializers

from ..models import Cart, Item

from .items import ItemSerializer, ItemCreateSerializer


class CartItemSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('items',)


class CartItemAddSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    items = ItemCreateSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'user',
            'items',
        )

    def create(self, validated_data):
        items = validated_data.pop('items')
        cart, created = Cart.objects.get_or_create(**validated_data)
        for i in items:
            item = Item.objects.create(**i)
            cart.items.add(item)
        return cart
