# Generated by Django 4.0.1 on 2022-03-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0041_rename_data_chart_averagepackage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='messagebox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2022-03-31')),
                ('title', models.CharField(default='', max_length=50)),
                ('link', models.CharField(blank=True, default='', max_length=300)),
            ],
        ),
    ]