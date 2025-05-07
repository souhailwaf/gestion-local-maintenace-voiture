from django.contrib import admin
from .models import Vehicule

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('marque', 'immatricule', 'client', 'date_creation', 'derniere_maintenance')
    search_fields = ('marque', 'immatricule', 'client__nom', 'client__prenom')
    list_filter = ('date_creation', 'derniere_maintenance')
