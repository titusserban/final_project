from django.urls import path

from Posts import views
from Posts.views import homepage

app_name = 'Posts'

urlpatterns = [
    path('', homepage, name="homepage")
]