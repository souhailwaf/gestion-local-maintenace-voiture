from django.db import models
from vehicules.models import Vehicule
from mecaniciens.models import Mecanicien
from clients.models import Client
ETAT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('en_pause', 'En pause'),
        ('termine', 'Terminé'),
        ('annule', 'Annulé'),
    ]
class Reparation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, related_name='reparations')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reparations', null=True, blank=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='en_attente')
    mecanicien = models.ForeignKey(Mecanicien, on_delete=models.SET_NULL, null=True, related_name='reparations')
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    notes_mecanicien = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"Réparation de {self.vehicule} - {self.etat}"

    def save(self, *args, **kwargs):
        # S'assurer que le client correspond au véhicule
        if not self.client_id and self.vehicule:
            self.client = self.vehicule.client
        super().save(*args, **kwargs)