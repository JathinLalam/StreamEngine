
from django.urls import path
from .views import home, success

urlpatterns = [
    path('<int:video_prize>', home, name='home'),
    path('success' , success , name='success')
]