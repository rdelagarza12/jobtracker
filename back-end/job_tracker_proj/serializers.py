from rest_framework import serializers
from job_app.models import Job
from tracker_app.models import Tracker
from tracker_library_app.models import TrackerLibrary
import json
from django.core.serializers import serialize

#<------- JOB SERIALIZER

class JobSerializer(serializers.ModelSerializer):


    # FORMAT HOW WE WANT TO RECEIVE THE INFORMATION
    class Meta:
        model = Job
        fields = [
            "id",
            "job_name",
            "company_name",
            "job_description",
            "date_applied",
            "contact_info",
            "application_status",
            "tracker"
        ]

# <------ TRACKER SERIALIZERS
class TrackerSerializer(serializers.ModelSerializer):
    # TO HAVE NESTED RELATIONSHIP DATA MEMBERS WE NEED TO SERIALIZE THEM WITHIN THE CLASS
    applied_jobs = serializers.SerializerMethodField()

    class Meta:
        model = Tracker
        fields = [
            "id", 
            "name", 
            "library",
            "applied_jobs"
            ]
        
        # CREATE METHOD TO SERIALIZE IT, ENSURE IT MATCHES THE NAME ON THE NAME DECLARED LN 29
    def get_applied_jobs(self, instance):
        all_jobs = []
        for job in instance.job.all():
            serialized_job = JobSerializer(job).data
            all_jobs.append(serialized_job)
        return all_jobs

# < ----- LIBRARY TRACKER SERIALIZER

class TrackerLibrarySerializer(serializers.ModelSerializer):
    active_trackers = serializers.SerializerMethodField()
    class Meta:
        model = TrackerLibrary
        fields = [
            'id', 
            'user',
            'active_trackers'
            ]
        
    def get_active_trackers(self, instance):
        all_trackers = []
        for tracker in instance.tracker.all():
            formatted_tracker = {
                "id" : tracker.id,
                "name" : tracker.name,
                "applied_jobs" : len(tracker.job.all())
            }
            all_trackers.append(formatted_tracker)
        return all_trackers