# Generated by Django 3.1.2 on 2021-02-18 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnwdata', '0012_auto_20210217_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='avgprice',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='marketindex',
            field=models.IntegerField(null=True),
        ),
    ]
