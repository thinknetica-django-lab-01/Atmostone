# Generated by Django 3.1.4 on 2021-02-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0009_auto_20210211_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscription',
            field=models.CharField(choices=[('N', 'None'), ('H', 'Subscribe to new Hotels')], default='N', max_length=1),
        ),
    ]
