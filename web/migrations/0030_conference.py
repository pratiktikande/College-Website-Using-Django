# Generated by Django 4.0.1 on 2022-03-20 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0029_placementstestquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('link', models.CharField(default='', max_length=500)),
                ('year', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
