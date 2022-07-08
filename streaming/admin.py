from django.contrib import admin
from .models import video, purchased, userdetails
# Register your models here.


admin.site.register(video)
admin.site.register(purchased)
admin.site.register(userdetails)