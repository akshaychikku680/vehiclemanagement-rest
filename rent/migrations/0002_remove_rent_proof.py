# Generated by Django 4.2.4 on 2023-09-08 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='proof',
        ),
    ]