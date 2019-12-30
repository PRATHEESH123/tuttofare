# django rest framework
from rest_framework import serializers

# local
from ..models import Order

# local serializers
from .items import ItemSerializer  # TODO check if this is correct


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
