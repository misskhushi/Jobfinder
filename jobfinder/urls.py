"""jobfinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('admin_login', admin_login, name="admin_login"),
    path('admin_home', admin_home, name="admin_home"),
    path('user', user, name="user"),
    path('user_signup', user_signup, name="user_signup"),
    path('user_home', user_home, name="user_home"),
    path('recruiter', recruiter, name="recruiter"),
    path('recruiter_signup', recruiter_signup, name="recruiter_signup"),
    path('Logout', Logout, name="Logout"),
    path('view_users', view_users, name="view_users"),
    path('delete_user/<int:pid>', delete_user, name="delete_user"),
    path('recruiter_pending', recruiter_pending, name="recruiter_pending"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)