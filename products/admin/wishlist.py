from django.contrib import admin

# local
from ..models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    '''Admin View for Wishlist'''

    list_display = ('user',)
    filter_horizontal = ('products',)
