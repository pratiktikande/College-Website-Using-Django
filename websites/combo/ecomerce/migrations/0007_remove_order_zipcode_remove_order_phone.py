# Generated by Django 4.0.1 on 2022-01-23 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0006_remove_order_zip_order_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Zipcode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
    ]