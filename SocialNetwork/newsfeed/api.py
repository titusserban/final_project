import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from newsfeed.models import Feed, Like


@login_required
def api_add_post(request):
    data = json.loads(request.body)
    body = data['body']
    post = Feed.objects.create(body=body, created_by=request.user)
    return JsonResponse({'success': True})


@login_required
def api_add_like(request):
    data = json.loads(request.body)
    post_id = data['post_id']
    if not Like.objects.filter(post_id=post_id).filter(created_by=request.user).exists():
        #verificam daca userul nu a dat like
        like = Like.objects.create(post_id=post_id, created_by=request.user)
    return JsonResponse({'success': True})

@login_required
def api_remove_like(request):
    data = json.loads(request.body)
    print(data)
    post_id = data['post_id']
    if Like.objects.filter(post_id=post_id).filter(created_by=request.user).exists():
        #verificam daca userul a dat like
        liked_post = Like.objects.filter(post_id=post_id).filter(created_by=request.user)
        liked_post.delete()
    return JsonResponse({'success': True})
