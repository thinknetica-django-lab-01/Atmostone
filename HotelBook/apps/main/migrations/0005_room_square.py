# Generated by Django 2.2 on 2021-01-24 02:01
import random

from django.db import migrations, models



class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_auto_20210122_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_square',
            field=models.DecimalField(decimal_places=1, max_digits=10),
            preserve_default=False,
        )
    ]
