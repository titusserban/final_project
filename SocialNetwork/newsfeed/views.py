from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Feed

# Create your views here.

@login_required
def newsfeed1(request):
    user_ids = [request.user.id]

    for postuser in request.user.userprofile.follows.all():
        user_ids.append(postuser.user.id)

    posts = Feed.objects.filter(created_by_id__in = user_ids)

    for post in posts:
        likes = post.likes.filter(created_by_id=request.user.id)
        if likes.count() > 0:
            post.liked = True
        else:
            post.liked = False

    return render(request, 'newsfeed/newsfeed12.html', {'posts': posts})


@login_required
def search(request):
    query = request.GET.get("query", "")
    if len(query) > 0:
        postusers = User.objects.filter(username__icontains=query)
    else:
        postusers = []
    context = {
        "query": query,
        "postusers": postusers
    }
    return render(request, "newsfeed/search.html", context)



