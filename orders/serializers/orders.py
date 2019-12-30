# django rest framework
from rest_framework import serializers

# apps
from products.serializers import ProductSerializer

# local
from ..models import Order, Item


class ItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Item
        fields = (
            'product',
            'quantity',
        )


class OrderSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True, read_only=True)
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
            'user',
            'items',
            'created',
            'fulfillment_status',
            'payment_status',
            'payment_type',
            'shipping_address',
        )
