# Generated by Django 3.1.4 on 2021-01-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210112_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default=False, max_length=500),
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
    ]