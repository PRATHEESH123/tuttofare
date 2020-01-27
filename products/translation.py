# third party
from modeltranslation.translator import register, TranslationOptions

# local
from .models import Product , Category , Brand , Collection , Tag


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'descrption',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Collection)
class CollectionTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)
