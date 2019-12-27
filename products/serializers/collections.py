# django rest framework
from rest_framework import serializers

# local
from ..models import Collection, CollectionImage
from .products import ProductSerializer


class CollectionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollectionImage
        fields = (
            'id',
            'image',
            'alt',
        )

    def to_representation(self, instance):
        return self.context['request'].build_absolute_uri(instance.image.url)


class CollectionsSerializer(serializers.ModelSerializer):
    images = CollectionImageSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Collection
        fields = (
            'id',
            'name',
            'products',
            'images',
        )
