from rest_framework import viewsets

from ..models import CartItem
from ..serializers import CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
