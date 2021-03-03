# Generated by Django 3.1.7 on 2021-03-01 13:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_hotel_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='features',
        ),
        migrations.AddField(
            model_name='hotel',
            name='features',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), blank=True, default=['Feature1', 'Feature2'], size=None),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='HotelFeature',
        ),
    ]
