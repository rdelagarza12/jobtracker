# Generated by Django 5.0.1 on 2024-01-30 23:31

import django.db.models.deletion
import job_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0005_alter_job_tracker'),
        ('tracker_app', '0002_alter_tracker_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.TextField(blank=True, max_length=50, validators=[job_app.validators.validate_name]),
        ),
        migrations.AlterField(
            model_name='job',
            name='tracker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='tracker_app.tracker'),
        ),
    ]
