# Generated by Django 2.2.7 on 2020-01-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20191227_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='brand name')),
                ('logo', models.ImageField(upload_to='brands', verbose_name='brand logo')),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
        ),
    ]