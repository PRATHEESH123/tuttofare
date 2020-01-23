from rest_framework import serializers
from ..serializers import ProductSerializer
from ..models import Tag , Product

class TagSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model= Tag
        fields=(
            'id',
            'name',
            'products',
        )
