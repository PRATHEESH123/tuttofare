from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Order(models.Model):
    """Model definition for Order."""

    UNFULFILLED = 0
    FULFILLED = 1

    FULFILLMENT_CHOICES = (
        (UNFULFILLED, 'UNFULFILLED'),
        (FULFILLED, 'FULFILLED'),
    )

    PAID = 0
    UNPAID = 1

    PAYMENT_CHOICES = (
        (PAID, 'PAID'),
        (UNPAID, 'UNPAID'),
    )

    COD = 0
    CREDIT_CARD = 1

    PAYMENT_TYPE = (
        (COD, 'COD'),
        (CREDIT_CARD, 'CREDIT_CARD'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField('Item')
    created = models.DateTimeField(default=timezone.now, editable=False)
    fulfillment_status = models.IntegerField(
        choices=FULFILLMENT_CHOICES,
        default=UNFULFILLED,
        blank=True,
    )
    payment_status = models.IntegerField(
        choices=PAYMENT_CHOICES,
        default=UNPAID,
        blank=True,
    )
    payment_type = models.IntegerField(choices=PAYMENT_TYPE, default=COD)
    shipping_address = models.ForeignKey('Address', on_delete=models.PROTECT)

    def __str__(self):
        """Unicode representation of Order."""
        return f'<{self.user}> {self.id}'
