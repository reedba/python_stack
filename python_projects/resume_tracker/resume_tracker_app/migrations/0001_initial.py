# Generated by Django 3.1 on 2022-01-27 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('date_submitted', models.DateTimeField(null=True)),
                ('follow_up', models.DateTimeField(null=True)),
                ('poster_name', models.CharField(max_length=255)),
                ('poster_email', models.CharField(max_length=255)),
                ('poster_number', models.CharField(max_length=255)),
                ('skills', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('related_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_connection', to='resume_tracker_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Interview_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interviewer_name', models.CharField(max_length=255)),
                ('interviewer_email', models.CharField(max_length=255)),
                ('interviewer_phone', models.CharField(max_length=255)),
                ('interview_date', models.DateTimeField(null=True)),
                ('questions_asked', models.TextField()),
                ('questions_to_ask', models.TextField()),
                ('follow_up', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('related_resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_connection', to='resume_tracker_app.resume_submission')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_creator', to='resume_tracker_app.user'),
        ),
        migrations.AddField(
            model_name='company',
            name='user_favorite',
            field=models.ManyToManyField(related_name='favorited_company', to='resume_tracker_app.User'),
        ),
    ]
