from django.db import models


class Item(models.Model):
    """Model definition for Item."""

    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='+')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        """Unicode representation of Item."""
        return f'<{self.product}: {self.quantity}>'
