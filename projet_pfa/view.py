from pyexpat.errors import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

from administration import admin
from clients.models import Client
from mecaniciens.models import Mecanicien


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if Client.objects.filter(username=username, password=password).exists():
            client = Client.objects.get(username=username, password=password)
            login(request, client)
            return redirect('clients:profil', pk=client.id)
        elif Mecanicien.objects.filter(username=username, password=password).exists():
            mecanicien = Mecanicien.object.get(username=username, password=password)
            login(request,mecanicien)
            return redirect('mecanicien:dashboard',pk=mecanicien.pk)
       






def legout_view(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('clients:connexion')