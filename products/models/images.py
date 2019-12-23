from django.db import models


class ProductImage(models.Model):
    """Model definition for ProductImage."""

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('product images', upload_to='products')
    alt = models.CharField('alt text', max_length=50, null=True, blank=True)

    def __str__(self):
        """Unicode representation of ProductImage."""
        return f'{self.product.name}'