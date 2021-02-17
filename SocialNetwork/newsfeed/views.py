from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def newsfeed1(request):
    return render(request, 'newsfeed/newsfeed12.html')


