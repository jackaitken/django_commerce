# Generated by Django 3.1.4 on 2021-01-12 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210112_2148'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bids',
            new_name='Bid',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]