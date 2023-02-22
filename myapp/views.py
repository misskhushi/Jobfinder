from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date

# Create your views here.
def index(request):
    return render(request,'index.html')

def admin_login(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes" 
    d = {'error':error}
    return render(request,'admin_login.html', d)

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = JobSeeker.objects.all()
    d = {'data':data}
    return render(request,'view_users.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='pending')
    d = {'data':data}
    return render(request,'recruiter_pending.html',d)

def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    recruiter = Recruiter.objects.get(id=pid)
    if request.method=="POST":
        s = request.POST['status']
        recruiter.status=s
        try:
            recruiter.save()
            error="no"
        except:
            error="yes"
    d = {'recruiter':recruiter, 'error':error}
    return render(request,'change_status.html',d)

def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Accept')
    d = {'data':data}
    return render(request,'recruiter_accepted.html',d)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Reject')
    d = {'data':data}
    return render(request,'recruiter_rejected.html',d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all
    d = {'data':data}
    return render(request,'recruiter_all.html',d)

def delete_recruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = User.objects.get(id=pid)
    recruiter.delete()
    return redirect('recruiter_all')

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n) 
                u.save()    
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passwordadmin.html',d)

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

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user')
    return render(request,'user_home.html')

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

def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n) 
                u.save()    
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passworduser.html',d)

def recruiter(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status!="pending":
                    login(request,user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error="yes"
    d = {'error':error}
    return render(request,'recruiter.html', d)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter')
    return render(request,'recruiter_home.html')

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
    return render(request,'recruiter_signup.html', d)


def Logout(request):
    logout(request)
    return redirect('index')

def change_passwordrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter')
    error=""
    if request.method=="POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n) 
                u.save()    
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passwordrecruiter.html',d)

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter')
    error = ""
    if request.method=='POST':
       jt = request.POST['jobtitle']
       stad = request.POST['startdate']
       endd = request.POST['enddate']
       sal = request.POST['salary']
       logo = request.FILES['logo']
       exp = request.POST['experience']
       loc = request.POST['location']
       skill = request.POST['skills']
       des = request.POST['description']
       user = request.user
       recruiter = Recruiter.objects.get(user=user)
       try:
          Job.objects.create(recruiter=recruiter, start_date=stad, end_date=endd, title=jt, salary=sal, image=logo, description=des, experience=exp, location=loc, skills=skill, creationdate=date.today())
          error="no"
       except:
           error="yes"
    d = {'error':error} 
    return render(request,'add_job.html', d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job':job}
    return render(request,'job_list.html', d)

def edit_jobdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter')
    error = ""
    job = Job.objects.get(id=pid)
    if request.method=='POST':
       jt = request.POST['jobtitle']
       stad = request.POST['startdate']
       endd = request.POST['enddate']
       sal = request.POST['salary']
       exp = request.POST['experience']
       loc = request.POST['location']
       skill = request.POST['skills']
       des = request.POST['description']
       
       job.title = jt
       job.salary = sal
       job.experience = exp
       job.location = loc
       job.skills = skill
       job.description = des
       try:
          job.save()
          error="no"
       except:
           error="yes"
       if stad:
            try:
                job.start_date = stad
                job.save()
            except:
                pass
       else:
            pass
       if endd:
            try:
                job.end_date = endd
                job.save()
            except:
                pass
       else:
            pass
    d = {'error':error, 'job':job} 
    return render(request,'edit_jobdetail.html', d)