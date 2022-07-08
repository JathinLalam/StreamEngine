import email
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Profile
import random
from django.core.mail import send_mail
import sys
# Create your views here.

def register(request):
    if(request.method == 'POST'):
        username1 = request.POST['username']
        email1 = request.POST['email']
        password1 = request.POST['password']
        confirm_password = request.POST['confirm_password']
        mobile = request.POST['mobile_number']
        print("Once")
        if password1 == confirm_password:
            print("password")
            if User.objects.filter(username=username1).exists():
                messages.warning(request, 'Username exists')
                return redirect('register')
            else:
                print("else")
                if User.objects.filter(email=email1).exists():
                    messages.warning(request, 'email already exists')
                    print(User.objects.filter(email=email1))
                    return redirect('register')
                else:
                    print("clear")
                    user = User.objects.create_user(username=username1, email=email1, password=password1)
                    user.save()
                    otp = str(random.randint(1000 , 9999))
                    profile = Profile(user = user , mobile=mobile, otp = otp, email=email1) 
                    profile.save()
                    request.session['mobile'] = mobile
                    request.session['email'] = email1
                    # messages.success(request, 'Account created successfully')
                    # return redirect('login')
                    try:
                        body = "Hey We are Happy to see that\n"+ username1 + " With email id  "+ email1 +"\nIs trying to login to StreamEngine \n\n"+ "Here's The OTP for veryfing ur account is : " + otp
                        send_mail("StreamEngine Site", body, "StreamEnginge@gmail.com", [email1] ,fail_silently=True)
                        print(body)
                    except:
                        e=sys.exc_info()[0]
                        print(e)
                    return redirect('otp')
        else:
            return redirect('register')
    else:
        return render(request, 'signup.html')

def otp(request):
    mobile = request.session['mobile']
    email = request.session['email']
    context = {'mobile':mobile,'email':email}
    
    if request.method == 'POST':
        otp = request.POST['otp']
        profile = Profile.objects.filter(mobile=mobile).first()
        
        if otp == profile.otp:
            return redirect('explore')
        else:
            print('Wrong')
            
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':mobile, 'email':email, }
            return render(request,'otp.html' , context)
            
        
    return render(request,'otp.html' , context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
           auth.login(request, user)
           return redirect('explore')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

def logout_user(request):
    auth.logout(request)
    return redirect('explore')


def forgotpassword(request):
    return render(request, 'forgotpassword.html')


def resetpassword(request):
    return render(request, 'resetpassword.html')