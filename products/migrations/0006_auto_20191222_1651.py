# Generated by Django 2.2.7 on 2019-12-22 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_varaint_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='varaint_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
