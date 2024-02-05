# Generated by Django 5.0.1 on 2024-01-31 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0006_job_job_description_alter_job_tracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='application_status',
            field=models.CharField(choices=[('AP', 'Applied'), ('RE', 'Rejected'), ('AC', 'Accepted'), ('UR', 'Under Review'), ('IN', 'Interviewing')], default='APPLIED', max_length=25),
        ),
    ]