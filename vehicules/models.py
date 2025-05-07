from django.db import models
from clients.models import Client

class Vehicule(models.Model):
    marque = models.CharField(max_length=100)
    immatricule = models.CharField(max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='vehicules')
    date_creation = models.DateTimeField(auto_now_add=True)
    derniere_maintenance = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.marque} {self.immatricule}"