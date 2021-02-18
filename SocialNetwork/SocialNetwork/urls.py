"""SocialNetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views
from django.urls import path, include


from Posts.views import homepage, signup
from Userprofile.views import userprofile, follow_user
from newsfeed.api import api_add_post
from newsfeed.views import newsfeed1, search

urlpatterns = [
    path('', views.LoginView.as_view(template_name='Registration/login.html'), name='login'),
    path('homepage/', homepage, name='homepage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('newsfeedpage/', newsfeed1, name='newsfeedpage'),
    path('api/add_post/', api_add_post, name='api_add_post'),
    path('search/', search, name='search'),
    path('u/<str:username>/', userprofile, name='userprofile'),
    path('u/<str:username>/follow/', follow_user, name='follow_user'),
    path('admin/', admin.site.urls),


]
