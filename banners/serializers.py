# 3rd party
from rest_framework import serializers

# local
from .models import Banner, BannerImage


class BannerImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BannerImage
        fields = ('image',)


class BannerSerializer(serializers.ModelSerializer):

    images = BannerImageSerializer(many=True)

    class Meta:
        model = Banner
        fields = (
            'id',
            'name',
            'images',
        )
