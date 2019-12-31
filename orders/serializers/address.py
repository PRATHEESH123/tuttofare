from rest_framework import serializers

# local
from ..models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'id',
            'first_name',
            'last_name',
            'line1',
            'line2',
            'line3',
            'city',
            'phone',
            'postalcode',
        )
