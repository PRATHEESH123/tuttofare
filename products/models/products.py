from django.db import models


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField('product name', max_length=50)
    descrption = models.TextField(default='')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    varaint_of = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Unicode representation of Product."""
        return f'{self.name}'

    def average_rating(self):
        result = self.reviews.all().aggregate(rating=models.Avg('rating'))
        return result['rating']