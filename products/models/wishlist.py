from django.db import models


class Wishlist(models.Model):
    """Model definition for Wishlist."""

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product')

    def __str__(self):
        """Unicode representation of Wishlist."""
        return f'[{self.user}]'
