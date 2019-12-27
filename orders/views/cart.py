from rest_framework import viewsets

from ..models import Cart
from ..serializers import CartItemSerializer, CartItemAddSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CartItemAddSerializer
        return super().get_serializer_class()
