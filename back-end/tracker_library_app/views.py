from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from job_tracker_proj.serializers import TrackerLibrarySerializer
from tracker_app.models import Tracker
# Create your views here.
class User_Authentication(APIView):
    authentication_classess = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class My_Library(User_Authentication):

    # RETURNS AN ENTIRE LIBRARY FROM THE USER
    def get(self, request):
        library = request.user.library
        serialized_library = TrackerLibrarySerializer(library).data
        return Response(serialized_library)
    

    #CREATES A NEW TRACKER IN THE USERS LIBRARY
    def post(self, request):
        library = request.user.library
        try:
            tracker_name = request.data.get("name")
            new_tracker = Tracker(name=tracker_name, library=library)
            new_tracker.save()
            return Response({'id' : new_tracker.id, 'name': new_tracker.name, 'applied_jobs' : 0},HTTP_201_CREATED)
        except:
            return Response("Invalid Tracker Name", status=HTTP_404_NOT_FOUND)
        

class Delete_Single_Tracker(User_Authentication):
    
    def delete(self, request, tracker_id):
        library = request.user.library
        try:
            deleting_tracker = library.tracker.get(id=tracker_id)
            deleting_tracker.delete()
            return Response(HTTP_204_NO_CONTENT)
        except:
            return Response("Tracker does not exist", status=HTTP_404_NOT_FOUND)

