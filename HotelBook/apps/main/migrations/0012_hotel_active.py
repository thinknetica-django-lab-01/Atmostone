# Generated by Django 3.1.6 on 2021-02-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210219_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
