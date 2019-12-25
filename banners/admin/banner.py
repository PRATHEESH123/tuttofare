from django.contrib import admin

# local
from ..models import Banner, BannerImage


class BannerImageInline(admin.TabularInline):
    model = BannerImage
    extra = 1


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    '''Admin View for Banner'''

    list_display = ('name',)
    inlines = [
        BannerImageInline,
    ]
