# Generated by Django 4.2.4 on 2023-09-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechile', '0002_alter_vechile_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vechile',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]
