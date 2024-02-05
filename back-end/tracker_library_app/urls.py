from django.urls import path, include
from .views import My_Library, Delete_Single_Tracker

urlpatterns = [
    path("", My_Library.as_view(), name="my_library"),
    path("<int:tracker_id>/", Delete_Single_Tracker.as_view(), name="delete_single_tracker")
]