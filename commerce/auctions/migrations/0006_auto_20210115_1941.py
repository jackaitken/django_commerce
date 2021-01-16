# Generated by Django 3.1.4 on 2021-01-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210115_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='comments',
        ),
        migrations.AddField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(related_name='listing_comment', to='auctions.Comment'),
        ),
    ]
