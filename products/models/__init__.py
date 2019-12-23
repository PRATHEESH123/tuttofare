from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from django.utils import timezone


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField('product name', max_length=50)
    descrption = models.TextField(default='')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    in_stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    varaint_of = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Unicode representation of Product."""
        return f'{self.name}'


class ProductImage(models.Model):
    """Model definition for ProductImage."""

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('product images', upload_to='products')
    alt = models.CharField('alt text', max_length=50, null=True, blank=True)

    def __str__(self):
        """Unicode representation of ProductImage."""
        return f'{self.product.name}'


class ProductReview(models.Model):
    """Model definition for ProductReview."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    rating = models.PositiveIntegerField()
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Unicode representation of ProductReview."""
        return f'{self.user}: {self.text}'


class Category(MPTTModel):
    """Model definition for Category."""

    name = models.CharField(
        'Category Name',
        max_length=50,
    )
    cover = models.ImageField(
        'Cover Photo',
        null=True,
        blank=True,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    class MPTTMeta:
        """Meta definition for Category."""
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return f'{self.name}'  # TODO
