# Generated by Django 3.1.4 on 2021-01-18 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_user_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='watchlist',
        ),
    ]
