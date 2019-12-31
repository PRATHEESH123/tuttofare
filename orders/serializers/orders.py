# django rest framework
from rest_framework import serializers

# local
from ..models import Order, Item

# local serializers
from .items import ItemSerializer, ItemCreateSerializer  # TODO check if this is correct


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    items = ItemCreateSerializer(many=True)  # need here to setup proper validation

    class Meta:
        model = Order
        fields = (
            'user',
            'items',
            'payment_type',
            'shipping_address',
        )

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for i in items:
            print(i)
            item = Item.objects.create(**i)
            order.items.add(item)
        return order


class OrderSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True)
    payment_status = serializers.CharField(
        source='get_payment_status_display',
        read_only=True,
    )
    fulfillment_status = serializers.CharField(
        source='get_fulfillment_status_display',
        read_only=True,
    )
    payment_type = serializers.CharField(source='get_payment_type_display')

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'items',
            'created',
            'fulfillment_status',
            'payment_status',
            'payment_type',
            'shipping_address',
        )
