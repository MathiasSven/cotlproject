# Generated by Django 3.1.2 on 2020-12-22 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pnwdata', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='pay_on',
            new_name='payed_on',
        ),
    ]