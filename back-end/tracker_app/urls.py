from django.urls import path
from .views import All_Trackers, Single_Tracker, Single_Job


urlpatterns = [
    path("", All_Trackers.as_view(), name="all_trackers"),
    path("<int:tracker>/", Single_Tracker.as_view(), name="single_tracker"),
    path("<int:tracker>/<int:job_id>/", Single_Job.as_view(), name="single_job")
]