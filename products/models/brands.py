from django.db import models


class Brand(models.Model):
    """Model definition for Brand."""

    name = models.CharField('brand name', max_length=100)
    logo = models.ImageField('brand logo', upload_to='brands')
    products = models.ManyToManyField('products.Product')

    def __str__(self):
        """Unicode representation of Brand."""
        return f'{self.name}'
