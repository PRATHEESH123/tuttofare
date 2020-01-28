from django.db import models


class Tag(models.Model):
    """Model definition for Tag."""

    name = models.CharField('Tag name', max_length=50)
    products= models.ManyToManyField('Product', related_name='tags')

    def __str__(self):
        """Unicode representation of Tag."""
        return f'{self.name}'