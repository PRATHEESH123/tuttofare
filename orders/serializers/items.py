from rest_framework import serializers

# app
from products.serializers import ProductSerializer

# local
from ..models import Item


class ItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = (
            'product',
            'quantity',
        )


class ItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Item
        fields = (
            'id',
            'product',
            'quantity',
        )
