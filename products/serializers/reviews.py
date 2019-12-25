# django rest framework
from rest_framework import serializers

# local
from ..models import ProductReview


class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = ProductReview
        fields = (
            'id',
            'user',
            'product',
            'text',
            'rating',
            'posted_on',
        )
