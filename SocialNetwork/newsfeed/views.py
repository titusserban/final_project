from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render

# Create your views here.

# @login_required
def newsfeed1(request):
    return render(request, 'newsfeed_template/newsfeed12.html')


