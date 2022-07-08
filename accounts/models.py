from email import message
from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)
    email = models.CharField(max_length=50, default="mailid@gmail.com")
    def save(self, *args, **kwargs):
        # if self.mobile is not None:
        #     account_sid = 'ACfebdd65ff7957b475a6f1e4faf3232c7'
        #     auth_token = 'bba7e390ba91a316c2d922d44691f8e3'
        #     client = Client(account_sid, auth_token)

        #     message = client.messages.create(
        #         body=f"Congratulations Your account has beed created successfully and otp for login in is {self.otp}",
        #         from_='+19897189863',
        #         to= '+91'+self.mobile
        #     )
        # else:
        #     account_sid = 'AC33b4e34a7e5c7ea0d6c9528b349d9cc8'
        #     auth_token = 'be23ba82eb617c3d17a3839ae0829c82'
        #     client = Client(account_sid, auth_token)

        #     message = client.messages.create(
        #         body=f"Sorry Your account has not created successfully",
        #         from_='+19897189863',
        #         to= self.mobile
        #     )

        # print(message.sid)
        return super().save(*args, **kwargs)