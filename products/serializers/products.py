# django rest framework
from rest_framework import serializers
from rest_framework.fields import empty

# local utils
from utils.mixins import DynamicSerializerMixin

# local
from ..models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = (
            'id',
            'image',
            'alt',
        )

    def to_representation(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)


class ProductSerializer(DynamicSerializerMixin, serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    rating = serializers.IntegerField(default=10)  # should start from 10
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = (
            'id',
            'url',
            'name',
            'price',
            'rating',
            'stock',
            'category',
            'images',
        )
        detail_fields = ('descrption',)
