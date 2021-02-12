from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

# from Posts.models import SocialNetworkDB
#
#
# class HomeIndex(ListView):
#     model = SocialNetworkDB
#     template_name = 'Posts/homepage.html'
#     context_object_name = 'all_posts'


def homepage(request):
    return render(request, 'Posts/homepage.html')
