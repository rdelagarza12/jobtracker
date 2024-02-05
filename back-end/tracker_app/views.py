from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from .models import Tracker
from job_app.models import Job
from job_tracker_proj.serializers import TrackerSerializer, JobSerializer
from datetime import date
# Create your views here.
class User_Authentication(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class All_Trackers(User_Authentication):

    # GRAB ALL TRACKERS IN A USER LIBRARY
    def get(self, request):
        all_trackers = request.user.library.tracker.all()
        serialized_trackers = [TrackerSerializer(tracker).data for tracker in all_trackers]
        return Response(serialized_trackers)
    
class Single_Tracker(User_Authentication):

    # GET ALL THE INFO ON A SINGLE TRACKER
    def get(self, request, tracker):
        try:
            single_tracker = get_object_or_404(Tracker, id=tracker)
            return Response(TrackerSerializer(single_tracker).data)            
        except:
            return Response("Tracker does not exist", status=HTTP_404_NOT_FOUND)


    # UPDATE A SINGLE TRACKER BY CREATING A NEW JOB WITHIN IT
    def post(self, request, tracker):
        # GRAB THE PLAYLIST THAT NEEDS TO BE UPDATED
        try:
            updating_tracker = get_object_or_404(Tracker, id=tracker)
        except:
            return Response("Tracker does not exist", status=HTTP_404_NOT_FOUND)
        # CREATE A JOB
        job_name=request.data.get("job_name")
        company_name=request.data.get("company_name")
        job_description=request.data.get("job_description", "")
        date_applied=request.data.get("date_applied", date.today())
        contact_info=request.data.get("contact_info", "")
        application_status=request.data.get("application_status", "APPLIED")
        try:
            new_job = Job(
                job_name=job_name,
                company_name=company_name,
                job_description=job_description,
                date_applied=date_applied,
                contact_info=contact_info,
                application_status=application_status,
                tracker=updating_tracker
            )
            new_job.save()
            return Response(new_job.id, status=HTTP_201_CREATED)
        except:
            return Response("Could not create Job Object, improper arguments", status=HTTP_404_NOT_FOUND)
        
        

    #UPDATE TRACKER NAME
    def put(self, request, tracker):
        try:
            updating_tracker = get_object_or_404(Tracker, id=tracker)
        except:
            return Response("Tracker does not exist", status=HTTP_404_NOT_FOUND)
        try:
            new_name = request.data.get("job_name")
            updating_tracker.name = new_name
            updating_tracker.save()
            return Response(HTTP_204_NO_CONTENT)
        except:
            return Response("Input is invalid", HTTP_404_NOT_FOUND)

class Single_Job(User_Authentication):

    #GET A SINGLE JOB
    def get(self, request, tracker, job_id):
        try:
            # ensures we are grabbing the right tracker
            tracker = get_object_or_404(Tracker, id=tracker)
        except:
            return Response("Tracker does not exist", status=HTTP_404_NOT_FOUND)
        try:
            # uses the tracker from before and checks linked jobs within it
            job = tracker.job.get(id=job_id)
            serialized_job = JobSerializer(job).data
            return Response(serialized_job)
        except:
            return Response("Job does not exist within this tracker", status=HTTP_404_NOT_FOUND)
        

    #UPDATE A SINGLE JOB
    def put(self, request, tracker, job_id):
        try:
            tracker = get_object_or_404(Tracker, id=tracker)
        except:
            return Response("Tracker does not exist", status=HTTP_404_NOT_FOUND)
        try:
            updating_job = tracker.job.get(id=job_id)
        except:
            return Response("Job does not exist within this tracker", status=HTTP_404_NOT_FOUND)
        if "job_name" in request.data:
            updating_job.job_name = request.data.get("job_name")
        if "company_name" in request.data:
            updating_job.company_name = request.data.get("company_name")
        if "date_applied" in request.data:
            updating_job.date_applied = request.data.get("date_applied")
        if "job_description" in request.data:
            updating_job.job_description = request.data.get("job_description")
        if "contact_info" in request.data:
            updating_job.contact_info = request.data.get("contact_info")
        if "application_status" in request.data:
            updating_job.application_status = request.data.get("application_status")
        updating_job.save()

        return Response(status=HTTP_204_NO_CONTENT)

    # DELETE A JOB FROM THE TRACKER
    def delete(self, request, tracker, job_id):
        try:
            updating_tracker = get_object_or_404(Tracker, id=tracker)
        except:
            return Response("Tracker does not exist", status=HTTP_404_NOT_FOUND)
        try:
            # CHECK TO SE IF JOB EXISTS WITHIN THIS TRACKER
            removing_job = updating_tracker.job.get(id=job_id)
            removing_job.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except:
            return Response("This Job does not exist", HTTP_404_NOT_FOUND)
