# Generated by Django 3.1 on 2022-01-28 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interview_details',
            old_name='follow_up',
            new_name='interview_follow_up',
        ),
    ]
