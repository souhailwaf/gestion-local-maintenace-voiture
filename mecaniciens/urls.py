from django.urls import path
from . import views
app_name = 'mecaniciens'
urlpatterns = [

    path('dashboard/', views.mecanicien_dashboard, name='mecanicien_dashboard'),


]