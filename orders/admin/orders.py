from django.contrib import admin

from ..models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = (
        'user',
        'created',
        'payment_status',
        'fulfillment_status',
        'payment_type',
        'shipping_address',
    )

    filter_horizontal = ('items',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return (
                'user',
                'payment_type',
            )
        else:
            return []
