from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Feed(models.Model):
    objects = None
    body = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        #aceasta clasa ordoneaza posturile de la cele mai recente la cele mai vechi


class Like(models.Model):
    objects = None
    post = models.ForeignKey(Feed, related_name="likes", on_delete=models.CASCADE)
    #cand stergem un post, se va sterge si like-ul
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
