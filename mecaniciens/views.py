

# Create your views here.

from urllib import request
from django.shortcuts import render


def liste_rendez_vous():
    return render(request, 'mecanicien/liste_rendez_vous.html')
def mecanicien_dashboard(request):
    return render(request,'mecanicien/dashboard.html')

def liste_reparation():
    return render(request, 'mecanicien/liste_reparation.html')


