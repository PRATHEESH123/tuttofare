from django.db import models


class Collection(models.Model):
    """Model definition for Collection."""

    name = models.CharField('collection name', max_length=50)
    products = models.ManyToManyField('Product')
    active = models.BooleanField(default=True)

    def __str__(self):
        """Unicode representation of Collection."""
        return f'{self.name}'



