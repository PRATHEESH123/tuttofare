# third party
from modeltranslation.translator import register, TranslationOptions

# local
from .models import Banner


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('name',)

