from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CharField)
    #Cand stergem userul, se sterge si userprofile
    follows = models.ManyToManyField('self', related_name="followed_by", symmetrical=False)
    #Cand un user 'follows' un alt user, nu inseamna ca automat va fi 'followed' inapoi


User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
#Cu ajutorul functii lambda se creaza obiectul User cand un user signs-up