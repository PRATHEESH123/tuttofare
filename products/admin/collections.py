from django.contrib import admin

# local
from ..models import Collection, CollectionImage


class ImageInline(admin.TabularInline):
    model = CollectionImage
    extra = 1


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    '''Admin View for Collection'''

    list_display = ('name',)
    filter_horizontal = ('products',)
    inlines = [
        ImageInline,
    ]