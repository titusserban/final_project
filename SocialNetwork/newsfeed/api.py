import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from newsfeed.models import Feed


@login_required
def api_add_post(request):
    data = json.loads(request.body)
    body = data['body']
    post = Feed.objects.create(body=body, created_by=request.user)

    return JsonResponse({'success': True})
