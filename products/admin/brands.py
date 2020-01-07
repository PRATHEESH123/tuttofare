from django.contrib import admin

from ..models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    '''Admin View for Brand'''

    list_display = ('name',)
    filter_horizontal = ('products',)