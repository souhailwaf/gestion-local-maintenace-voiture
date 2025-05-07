from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    # Client registration and authentication
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    
    # Client profile
    path('profil/<int:pk>/', views.profil, name='profil'),
    path('profil/<int:pk>/modifier/', views.modifier_profil, name='modifier_profil'),
    
    # Vehicle management
    path('vehicules/<int:pk>/', views.mes_vehicules, name='mes_vehicules'),
    path('vehicules/<int:pk>/ajouter/', views.ajouter_vehicule, name='ajouter_vehicule'),
    path('vehicules/<int:pk>/<int:vehicule_pk>/', views.details_vehicule, name='details_vehicule'),
]
