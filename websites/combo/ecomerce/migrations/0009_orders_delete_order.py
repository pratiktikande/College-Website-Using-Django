# Generated by Django 4.0.1 on 2022-01-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0008_order_zipcode_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=111)),
                ('address', models.CharField(max_length=111)),
                ('city', models.CharField(max_length=111)),
                ('state', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
            ],
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]