# Generated by Django 2.2.7 on 2019-12-27 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20191227_1628'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Item',
            new_name='CartItem',
        ),
    ]