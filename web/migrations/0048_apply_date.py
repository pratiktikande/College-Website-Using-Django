# Generated by Django 4.0.1 on 2022-03-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0047_remove_apply_id_apply_apply_id_alter_apply_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='date',
            field=models.DateField(default='2000-12-31'),
        ),
    ]