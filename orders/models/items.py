from django.db import models
from django.contrib.auth import get_user_model


class CartItem(models.Model):
    """Model definition for Item."""

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name='cart')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        """Unicode representation of Item."""
        return f'<{self.product}: {self.quantity}>'
