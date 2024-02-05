from django.urls import path
from .views import All_Jobs

urlpatterns = [
    path("", All_Jobs.as_view(), name="all_jobs")
]