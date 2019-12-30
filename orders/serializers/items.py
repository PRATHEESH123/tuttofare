from rest_framework import serializers

# app
from products.serializers import ProductSerializer

# local
from ..models import Item


class ItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Item
        fields = (
            'product',
            'quantity',
        )
