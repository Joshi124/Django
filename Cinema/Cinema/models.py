from django.db import models

# Create your models here.

class Cinemas(models.Model):
    Movie_Name = models.CharField(max_length=50)
    Actor_Character_Name = models.CharField(max_length=50)
    Actress_Character_Name = models.CharField(max_length=50)
    Actor_Name = models.CharField(max_length=50)
    Actress_Name = models.CharField(max_length=50)

