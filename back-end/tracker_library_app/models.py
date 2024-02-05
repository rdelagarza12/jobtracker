from django.db import models
from user_login_app.models import User
# Create your models here.

class TrackerLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="library")

    def __str__(self):
        return f"{self.user}'s Library"