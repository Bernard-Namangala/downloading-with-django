# Generated by Django 3.0.8 on 2020-07-31 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0004_auto_20200731_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='download_count',
            field=models.IntegerField(default=0),
        ),
    ]
