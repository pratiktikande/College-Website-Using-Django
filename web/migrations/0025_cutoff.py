# Generated by Django 4.0.1 on 2022-03-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_calender'),
    ]

    operations = [
        migrations.CreateModel(
            name='cutoff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=500)),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
