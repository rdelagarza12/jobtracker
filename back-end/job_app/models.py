from django.db import models
from datetime import date
from .validators import validate_name
from tracker_app.models import Tracker
# Create your models here.
class Job(models.Model):
    APPLIED = 'AP'
    REJECTED = 'RE'
    ACCEPTED = 'AC'
    UNDER_REVIEW = 'UR'
    INTERVIEWING = 'IN'

    APPLICATION_STATUS_CHOICES = [
        (APPLIED, 'Applied'),
        (REJECTED, 'Rejected'),
        (ACCEPTED, 'Accepted'),
        (UNDER_REVIEW, 'Under Review'),
        (INTERVIEWING, 'Interviewing'),
    ]

    job_name = models.CharField(max_length=100, validators=[validate_name])
    company_name = models.CharField(max_length=100, validators=[validate_name])
    job_description = models.TextField(max_length=50, validators=[validate_name], blank=True)
    date_applied = models.DateField(default=date.today, blank=True)
    contact_info = models.CharField(max_length=50, blank=True)
    application_status = models.CharField(max_length=25, choices=APPLICATION_STATUS_CHOICES, default="APPLIED")
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE, related_name="job", default=1)


    def __str__(self):
        return f"{self.job_name} : {self.application_status}"