from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout_user,name="logout"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
    path('restepassword',views.resetpassword,name="resetpassword"),
    path('otp' , views.otp , name="otp"),
]