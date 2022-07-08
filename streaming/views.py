from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import userdetails, purchased, video
# Create your views here.


def home(request):
    if not request.user.is_authenticated:
        trailers = video.objects.all().filter(video_price=0).filter(video_category="Trailers")
        movies = video.objects.all().filter(video_price=0).filter(video_category="Movies")
        series = video.objects.all().filter(video_price=0).filter(video_category="Series")
        params = {'trailers': trailers,
                  'movies': movies,
                  'series': series,
        }
    else:
        trailers = video.objects.all().filter(video_category="Trailers").order_by('-id')
        movies = video.objects.all().filter(video_category="Movies").order_by('-id')
        series = video.objects.all().filter(video_category="Series").order_by('-id')
        params = {'trailers': trailers,
                  'movies': movies,
                  'series': series,
        }
    return render(request, 'explore.html', params)

def watch_video(request, video_id):
    try:
        video_obj = video.objects.get(id=video_id)
        if not request.user.is_authenticated:
            all_videos = video.objects.all().filter(video_price=0)
            params = {'all_videos': all_videos}
        else:
            all_videos = video.objects.all().order_by('-id')
            params = {'all_videos': all_videos}
    except ObjectDoesNotExist:
        return render(request, '404.html')


    params = {'video': video_obj,
              'all_videos': all_videos,
              'user':User}
    return render(request, 'watch_video.html', params)