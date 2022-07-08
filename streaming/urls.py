from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name="explore"),
    path('dashboard',views.home,name="explore"),
    path('video/<int:video_id>/',views.watch_video,name="watch_video"),
]