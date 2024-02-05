from django.urls import path, include
from .views import Master_Sign_Up, Sign_Up, Log_In, Log_Out, Info
urlpatterns = [
    path('master/', Master_Sign_Up.as_view(), name="master"),
    path('signup/', Sign_Up.as_view(), name="signup"),
    path('login/', Log_In.as_view(), name="login"),
    path('logout/', Log_Out.as_view(), name="logout"),
    path('info/', Info.as_view(), name="info")
]