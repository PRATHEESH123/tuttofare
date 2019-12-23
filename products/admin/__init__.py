from django.contrib import admin

# 3rd party
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter

# local
from ..models import Category, Product, ProductImage, ProductReview


class SubCategoryInline(admin.StackedInline):
    model = Category
    extra = 0
    verbose_name = 'sub category'
    verbose_name_plural = 'sub categories'
    can_delete = False


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    '''Admin View for Category'''
    list_display = (
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    )
    list_display_links = ('indented_title',)
    inlines = [SubCategoryInline]


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0
    # verbose_name = 'sub category'
    # verbose_name_plural = 'sub categories'
    show_change_link = True


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('name', 'price', 'descrption')
    list_filter = (('category', TreeRelatedFieldListFilter),)
    inlines = [
        ProductImageInline,
        ProductReviewInline,
    ]
