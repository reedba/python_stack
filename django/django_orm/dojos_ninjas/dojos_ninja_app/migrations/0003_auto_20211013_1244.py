# Generated by Django 2.2 on 2021-10-13 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojos_ninja_app', '0002_auto_20211012_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='dojo',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='ninja',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ninja',
            name='updated_at',
        ),
    ]