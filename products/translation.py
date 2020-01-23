# third party
from modeltranslation.translator import register, TranslationOptions

# local
from .models import Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'descrption')
