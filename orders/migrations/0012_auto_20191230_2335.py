# Generated by Django 2.2.7 on 2019-12-30 23:35

from django.db import migrations


def delete_all_cart(apps, schema_editor):
    Cart = apps.get_model('orders', 'Cart')
    Cart.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20191230_2159'),
    ]

    operations = [
        migrations.RunPython(delete_all_cart),
    ]