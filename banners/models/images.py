from django.db import models


class BannerImage(models.Model):
    """Model definition for BannerImage."""

    banner = models.ForeignKey('Banner', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('banner image', upload_to='banner')

    class Meta:
        """Meta definition for BannerImage."""

        verbose_name = 'BannerImage'
        verbose_name_plural = 'BannerImages'

    def __str__(self):
        """Unicode representation of BannerImage."""
        return f'{self.banner.name }'
