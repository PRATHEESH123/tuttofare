# Generated by Django 2.2.7 on 2020-01-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_product_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='text_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='productreview',
            name='text_en',
            field=models.TextField(null=True),
        ),
    ]