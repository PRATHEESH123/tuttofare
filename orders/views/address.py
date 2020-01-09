from rest_framework import viewsets
from rest_framework import mixins

# local
from ..models import Address
from ..serializers import AddressSerializer


class AddressViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
