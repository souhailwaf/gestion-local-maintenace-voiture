
from django.db import models
from projet_pfa.clients.models import Client
from projet_pfa.vehicules.models import Vehicule
class Facture(models.Model):

    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicule =models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"Facture #{self.id} - {self.client.nom}"
    
