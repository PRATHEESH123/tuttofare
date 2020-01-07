from rest_framework import serializers

from utils.mixins import DynamicSerializerMixin

from ..models import Brand
from ..serializers import ProductSerializer


class BrandSerializer(DynamicSerializerMixin, serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Brand
        fields = (
            'id',
            'url',
            'name',
            'logo',
        )
        detail_fields = ('products',)
