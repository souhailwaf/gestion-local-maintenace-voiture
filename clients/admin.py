from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone', 'email', 'date_creation')
    search_fields = ('nom', 'prenom', 'telephone', 'email')
    list_filter = ('date_creation',)
