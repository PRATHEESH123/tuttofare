from django.db import models
from django.contrib.auth import get_user_model


class Cart(models.Model):
    """Model definition for Item."""

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField('Item')

    def __str__(self):
        """Unicode representation of Item."""
        return f'<{self.items}: {self.items}>'
