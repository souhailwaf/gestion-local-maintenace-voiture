from django.urls import path
from . import views

app_name = 'rendez_vous'

urlpatterns = [
    path('prendre/', views.prendre_rendez_vous, name='prendre_rendez_vous'),
    path('mes-rendez-vous/', views.mes_rendez_vous, name='mes_rendez_vous'),
    path('annuler/<int:pk>/', views.annuler_rendez_vous, name='annuler_rendez_vous'),
]
