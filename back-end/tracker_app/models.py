from django.db import models
from tracker_library_app.models import TrackerLibrary
from .validators import validate_tracker_name

# Create your models here.
class Tracker(models.Model):
    name = models.CharField(max_length=24, validators=[validate_tracker_name])
    library = models.ForeignKey(TrackerLibrary, on_delete=models.CASCADE, related_name="tracker")

    def __str__(self):
        return f"{self.name} tracker"