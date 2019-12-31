from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    """Model definition for Address."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100)
    line3 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = PhoneNumberField()
    postalcode = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Address."""

        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        """Unicode representation of Address."""
        return f'{self.first_name} {self.last_name}'
