from django.contrib import admin
from .models import Mecanicien

# Register your models here.
@admin.register(Mecanicien)
class MecanicienAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'experience', 'specialite')
    search_fields = ('nom', 'prenom', 'experience', 'specialite')
    list_filter = ('specialite',)

