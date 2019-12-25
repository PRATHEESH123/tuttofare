# 3rd party
from rest_framework import viewsets

# local
from .serializers import BannerSerializer
from .models import Banner


class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer