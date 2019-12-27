from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model


class Cart(models.Model):
    """Model definition for Cart."""

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of Cart."""
        return f'<Cart {self.user}>'


@receiver(post_save, sender=get_user_model())
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)