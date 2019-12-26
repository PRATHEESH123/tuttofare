from django.db import models
from django.db.models.signals import post_save

from django.conf import settings
from django.dispatch import receiver


class Wishlist(models.Model):
    """Model definition for Wishlist."""

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product', blank=True)

    def __str__(self):
        """Unicode representation of Wishlist."""
        return f'[{self.user}]'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_wishlist(sender, instance=None, created=False, **kwargs):
    if created:
        Wishlist.objects.create(user=instance)