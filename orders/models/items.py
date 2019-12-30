from django.db import models


class Item(models.Model):
    """Model definition for Item."""

    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        """Unicode representation of Item."""
        return f'<{self.product.name}>'
