# Generated by Django 4.0.1 on 2022-03-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_syllabus'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(default='', max_length=100)),
                ('link', models.CharField(default='', max_length=500)),
                ('sem', models.CharField(default='', max_length=100)),
                ('year', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
