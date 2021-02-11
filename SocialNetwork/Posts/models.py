from django.db import models

# Create your models here.

class SocialNetworkDB:
    #blank=True -> nu este mandatory in Django
    #null=True -> nu este mandatory in SQL
    content = models.TextField(blank=True, null=True)
    #Deoarece nu putem folosi SQL pentru stocarea de imagini,
    #trebuie folosit Media Storage Server(path-ul catre fisierul .jpg).
    image = models.FileField(upload_to="TBD", blank=True, null=True)

