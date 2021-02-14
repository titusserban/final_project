from django.urls import path

from newsfeed.views import newsfeed1

app_name = 'newsfeed'

urlpatterns = [
    path('', newsfeed1, name="newsfeed1"),

]