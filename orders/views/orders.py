# django
from django.shortcuts import get_object_or_404

# django rest framework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated
# local
from ..serializers import OrderSerializer, OrderCreateSerializer
from ..models import Order


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return super().get_serializer_class()

    @action(detail=True)
    def deliveried(self, request, pk):
        if not request.user.is_staff:
            raise NotAuthenticated('you need to staff')

        order = get_object_or_404(Order, pk=pk)
        order.fulfillment_status = Order.FULFILLED
        order.payment_status = Order.PAID
        order.save()
        return Response(self.get_serializer(order).data)