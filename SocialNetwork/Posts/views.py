from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'Posts/homepage.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('newsfeedpage')

    else:
        form = UserCreationForm()

    return render(request, 'Registration/signup.html', {'form': form})
