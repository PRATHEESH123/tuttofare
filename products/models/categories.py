from django.db import models

# 3rd  party
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """Model definition for Category."""

    name = models.CharField(
        'Category Name',
        max_length=50,
    )
    cover = models.ImageField(
        'Cover Photo',
        null=True,
        blank=True,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    class MPTTMeta:
        """Meta definition for Category."""
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return f'{self.name}'  # TODO
