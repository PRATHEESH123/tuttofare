# 3rd party
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# local
from ..models import Collection
from ..serializers import CollectionsSerializer


class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer
    permission_classes = [AllowAny]
