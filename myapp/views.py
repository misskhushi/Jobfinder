from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    return render(request,'admin_login.html')

def user(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = JobSeeker.objects.get(user=user)
                if user1.type == "jobseeker":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'user.html',d)

def recruiter(request):
    return render(request,'recruiter.html')

def recruiter_signup(request):
    error = ""
    if request.method=='POST':
       f = request.POST['fname']
       l = request.POST['lname']
       i = request.FILES['image']
       p = request.POST['pwd']
       company = request.POST['company']
       e = request.POST['email']
       c = request.POST['contact']
       g = request.POST['gender']
       try:
          user =  User.objects.create_user(first_name=f, last_name=l, username=e, password=p )
          Recruiter.objects.create(user=user, mobile=c, image=i,company=company, gender=g, type="recruiter", status="pending")
          error="no"
       except:
           error="yes"
    d = {'error':error}
    return render(request,'recruiter_signup.html')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request,'user_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def user_signup(request):
    error = ""
    if request.method=='POST':
       f = request.POST['fname']
       l = request.POST['lname']
       i = request.FILES['image']
       p = request.POST['pwd']
       e = request.POST['email']
       c = request.POST['contact']
       g = request.POST['gender']
       try:
          user =  User.objects.create_user(first_name=f, last_name=l, username=e, password=p )
          JobSeeker.objects.create(user=user, mobile=c, image=i, gender=g, type="jobseeker")
          error="no"
       except:
           error="yes"
    d = {'error':error}
    return render(request,'user_signup.html',d)
