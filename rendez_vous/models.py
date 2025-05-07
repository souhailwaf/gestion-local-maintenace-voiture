from django.db import models
from clients.models import Client
from vehicules.models import Vehicule

class RendezVous(models.Model):
    STATUS_CHOICES = [
        ('en_attente', 'En attente de confirmation'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
        ('termine', 'Terminé'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='rendez_vous')
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, related_name='rendez_vous')
    date_heure = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='en_attente')
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rendez-vous'
        verbose_name_plural = 'Rendez-vous'
        ordering = ['-date_heure']

    def __str__(self):
        return f"RDV {self.client} - {self.date_heure.strftime('%d/%m/%Y %H:%M')}"
