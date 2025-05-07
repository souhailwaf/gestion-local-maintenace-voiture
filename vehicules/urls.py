from django.urls import path
from . import views

app_name = 'vehicules'

urlpatterns = [
    # List all vehicles
    path('', views.vehicule_list, name='vehicule_list'),
    
    # View specific vehicle
    path('<int:pk>/', views.vehicule_detail, name='vehicule_detail'),
]
