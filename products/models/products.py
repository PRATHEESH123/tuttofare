from django.db import models


class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField('product name', max_length=50)
    sku=models.CharField('Sku Key', max_length=50, blank=True, unique=True)
    descrption = models.TextField(default='')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    varaint_of = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    false_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        """Unicode representation of Product."""
        return f'{self.name}'

    def average_rating(self):
        result = self.reviews.all().aggregate(rating=models.Avg('rating'))
        return result['rating'] or 0