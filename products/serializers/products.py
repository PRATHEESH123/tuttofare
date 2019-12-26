# django rest framework
from rest_framework import serializers
from rest_framework.fields import empty

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


class ProductSerializer(serializers.ModelSerializer):
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

    def get_field_names(self, declared_fields, info):
        a = super().get_field_names(declared_fields, info)
        detail_fields = getattr(self.Meta, 'detail_fields', None)

        if detail_fields is not None:
            return a + detail_fields
        return a
