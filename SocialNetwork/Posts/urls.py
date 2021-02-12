from django.urls import path

from Posts import views
from Posts.views import homepage

app_name = 'Posts'

urlpatterns = [
    # path('', views.HomeIndex.as_view(), name="homepage"),
    path('', homepage, name="homepage")
]