from django.contrib import admin

# Register your models here.
from user_login_app.models import User
from tracker_library_app.models import TrackerLibrary
from tracker_app.models import Tracker
from job_app.models import Job

admin.site.register([User, TrackerLibrary, Tracker, Job])