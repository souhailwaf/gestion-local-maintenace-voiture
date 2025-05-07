from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Mecanicien(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mecanicien')
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=10)
    experience = models.IntegerField()
    specialite = models.CharField(max_length=10)
    
