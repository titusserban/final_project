from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
