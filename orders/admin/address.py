from django.contrib import admin

# local
from ..models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    '''Admin View for Address'''

    list_display = (
        'first_name',
        'last_name',
        'phone',
        'postalcode',
    )
