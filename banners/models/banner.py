from django.db import models


class Banner(models.Model):
    """Model definition for Banner."""

    name = models.CharField('banner name', max_length=50)

    class Meta:
        """Meta definition for Banner."""

        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        """Unicode representation of Banner."""
        return f'{self.name}'
