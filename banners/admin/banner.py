from django.contrib import admin

# local
from ..models import Banner, BannerImage

from modeltranslation.admin import TranslationAdmin

class BannerImageInline(admin.TabularInline):
    model = BannerImage
    extra = 1


@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    '''Admin View for Banner'''

    list_display = ('name',)
    inlines = [
        BannerImageInline,
    ]
