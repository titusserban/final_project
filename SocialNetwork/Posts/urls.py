from django.urls import path

from Posts.views import homepage, signup

from django.contrib.auth import views

app_name = 'Posts'

# urlpatterns = (
#     path('homepage/', homepage, name='homepage'),
#     path('signup/', signup, name='signup'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),
#
# )