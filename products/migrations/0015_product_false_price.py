# Generated by Django 2.2.7 on 2020-01-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='false_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
