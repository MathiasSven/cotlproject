# Generated by Django 3.1.2 on 2021-02-25 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotlsite', '0011_remove_role_role_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membernation',
            name='discord_member',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cotlsite.member'),
        ),
    ]