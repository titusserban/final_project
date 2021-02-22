from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CharField)
    # OneToOneField ne permite sa avem mai multe profile
    #Cand stergem userul, se sterge si userprofile + este mandatory
    follows = models.ManyToManyField('self', related_name="followed_by", symmetrical=False)
    #ManyToManyField creaza un tabel in care putem grupa toate persoanele pe care userul le "urmareste"
    #symmetrical=False -> Cand un user 'follows' un alt user, nu inseamna ca automat va fi 'followed' inapoi
    avatar = models.ImageField(upload_to='uploads/', blank=True, null=True)
    #am instalat Pillow pentru a putea utiliza poze pentru avatar


User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
#Se creaza obiectul User cand un user signs-up