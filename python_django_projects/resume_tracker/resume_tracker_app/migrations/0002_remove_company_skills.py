# Generated by Django 3.1 on 2022-01-25 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='skills',
        ),
    ]
