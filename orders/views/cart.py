# django
from django.shortcuts import get_object_or_404

# django rest framework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Cart
from ..serializers import CartItemSerializer, CartItemAddSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CartItemAddSerializer
        return super().get_serializer_class()

    @action(detail=True)
    def decrement(self, request, pk):
        cart = get_object_or_404(self.get_queryset(), pk=pk)
        cart.quantity -= 1
        cart.save()
        return Response(self.get_serializer(cart).data)