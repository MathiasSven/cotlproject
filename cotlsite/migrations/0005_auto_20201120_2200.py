# Generated by Django 3.1.2 on 2020-11-21 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cotlsite', '0004_member_nation_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='nation_id',
        ),
        migrations.CreateModel(
            name='PnWData',
            fields=[
                ('nation_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nation_name', models.CharField(max_length=32, null=True)),
                ('leader_name', models.CharField(max_length=32, null=True)),
                ('flag_url', models.URLField(null=True)),
                ('date_founded', models.DateTimeField(null=True)),
                ('discord_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cotlsite.member')),
            ],
        ),
    ]
