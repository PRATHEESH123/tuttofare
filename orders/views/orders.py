# django rest framework
from rest_framework import viewsets

# local
from ..serializers import OrderSerializer
from ..models import Order


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
