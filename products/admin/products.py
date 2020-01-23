from django.contrib import admin

# MPTT
from mptt.admin import TreeRelatedFieldListFilter

# tranlations
from modeltranslation.admin import TranslationAdmin

# local
from ..models import Product, ProductImage, ProductReview


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    '''Admin View for Product'''

    list_display = ('name', 'price', 'stock', 'average_rating')
    list_filter = (('category', TreeRelatedFieldListFilter),)
    inlines = [
        ProductImageInline,
        ProductReviewInline,
    ]
