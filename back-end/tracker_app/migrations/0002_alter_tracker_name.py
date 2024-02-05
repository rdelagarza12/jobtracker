# Generated by Django 5.0.1 on 2024-01-30 02:22

import tracker_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='name',
            field=models.CharField(max_length=24, validators=[tracker_app.validators.validate_tracker_name]),
        ),
    ]
