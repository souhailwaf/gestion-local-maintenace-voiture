from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from clients.models import Client
from rendez_vous.models import RendezVous
from vehicules.models import Vehicule
from reparation.models import Reparation
#from rendez_vous.models import RendezVous
from mecaniciens.models import Mecanicien
from django.utils import timezone

class CustomAdminSite(admin.AdminSite):
    site_header = 'Administration Garage'
    site_title = 'Garage Admin'
    index_title = 'Tableau de bord'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_view(self.dashboard_view), name='admin-dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        context = {
            'total_clients': Client.objects.count(),
            'total_vehicules': Vehicule.objects.count(),
            'reparations_en_cours': Reparation.objects.filter(etat='En cours').count(),
            #'rendez_vous_aujourdhui': RendezVous.objects.filter(date__date=timezone.now().date()).count(),
            'total_mecaniciens': Mecanicien.objects.count(),
            'recent_activities': self.get_recent_activities(),
            **self.each_context(request),
        }
        return render(request, 'admin/dashboard.html', context)

    def get_recent_activities(self):
        reparations = Reparation.objects.select_related('vehicule', 'mecanicien').order_by('-date_debut')[:5]
        #rendez_vous = RendezVous.objects.select_related('client', 'vehicule').order_by('-date_creation')[:5]
        
        activities = []
        for rep in reparations:
            activities.append({
                'date': rep.date_debut,
                'client': rep.vehicule.client,
                'vehicule': rep.vehicule,
                'type': 'Réparation',
                'statut': rep.etat
            })
        #for rdv in rendez_vous:
        #    activities.append({
        #        'date': rdv.date_creation,
        #        'client': rdv.client,
        #        'vehicule': rdv.vehicule,
        #        'type': 'Rendez-vous',
        #        'statut': rdv.statut
        #    })
        
        return sorted(activities, key=lambda x: x['date'], reverse=True)[:10]

# Create custom admin site instance
admin_site = CustomAdminSite(name='admin')

# Register your models with the custom admin site
from django.contrib.auth.models import User, Group
admin_site.register(User)
admin_site.register(Group)

@admin.register(Client, site=admin_site)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'telephone', 'email', 'date_creation')
    search_fields = ('nom', 'prenom', 'telephone', 'email')
    list_filter = ('date_creation',)

@admin.register(Mecanicien, site=admin_site)
class MecanicienAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'experience', 'specialite')
    search_fields = ('nom', 'prenom', 'experience', 'specialite')
    list_filter = ('specialite',)

@admin.register(RendezVous, site=admin_site)
class RendzeVousAdmin(admin.ModelAdmin):
    list_display = ('client', 'vehicule', 'date_heure', 'status')
    search_fields = ('client', 'vehicule', 'date_heure', 'status')
    list_filter = ('date_creation',)

@admin.register(Reparation, site=admin_site)
class ReparationAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'date_debut', 'date_fin', 'etat', 'mecanicien', 'cout','date_creation','date_modification')
    search_fields = ('vehicule__marque', 'vehicule__immatricule', 'description','date_creation','date_modification')
    list_filter = ('etat', 'date_debut', 'date_fin')

