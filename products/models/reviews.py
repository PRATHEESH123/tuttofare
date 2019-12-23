from django.db import models
from django.utils import timezone


class ProductReview(models.Model):
    """Model definition for ProductReview."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='review')
    text = models.TextField()
    rating = models.PositiveIntegerField()
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Unicode representation of ProductReview."""
        return f'{self.user}: {self.text}'
