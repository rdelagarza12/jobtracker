from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_201_CREATED
from .models import Job
from job_tracker_proj.serializers import JobSerializer
# Create your views here.

class User_Authentication(APIView):
    authentication_classess = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class All_Jobs(User_Authentication):
    
    # GET ALL JOBS FROM A USER BY PLAYLIST
    def get(self, request):
        # fetches the trackers using the prefetch method and grabs related names that match our input
        all_trackers = request.user.library.tracker.prefetch_related('job')
        serialized_jobs = []
        for tracker in all_trackers:
            serialized_jobs.extend(JobSerializer(tracker.job.all(), many=True).data)
        return Response(serialized_jobs)