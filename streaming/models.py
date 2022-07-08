from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class video(models.Model):
    video_title = models.CharField(default="",max_length=100)
    video_link = models.URLField(max_length=1000)
    video_id = models.PositiveIntegerField()
    video_category = models.CharField(max_length=50)
    video_price = models.IntegerField(default=0)
    video_rating = models.FloatField(default=0.0)
    video_releasedate = models.DateTimeField()
    video_description = models.TextField(max_length=500)
    video_views = models.IntegerField()
    video_discount = models.IntegerField()
    video_thumbnail = models.ImageField(upload_to = 'images/')
    video_duration = models.TextField(default=1.10)

    def __str__(self):
        return self.video_title

class purchased(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.ForeignKey(video, on_delete=models.CASCADE)


# class payment_details(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     card_no = models.PositiveBigIntegerField()
#     expire_date = models.DateField()
#     name_of_the_card_holder = models.CharField()
#     upi_id = models.CharField()


class userdetails(models.Model):
    purchased_videos = models.ForeignKey(purchased, on_delete=models.CASCADE)
    #payment_details = models.ForeignKey(payment_details, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_verified = models.BooleanField(default=False)
