# Generated by Django 3.1.2 on 2021-11-26 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milestone', '0005_auto_20211126_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
    ]
