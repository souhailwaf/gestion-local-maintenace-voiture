from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from mecaniciens.models import Mecanicien
from .models import Client
from .form import ClientRegistrationForm, ClientUpdateForm
from vehicules.models import Vehicule
from vehicules.form import VehiculeForm


def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                # Vérifier le type d'utilisateur
                try:
                    client = Client.objects.get(user=user)
                    messages.success(request, f'Bienvenue {username}!')
                    return redirect('clients:profil', pk=client.pk)
                except Client.DoesNotExist:
                    try:
                        mecanicien = Mecanicien.objects.get(user=user)
                        messages.success(request, f'Bienvenue {username}!')
                        return redirect('mecaniciens:mecanicien_dashboard')
                    except Mecanicien.DoesNotExist:
                        if user.is_staff:
                            return redirect('admin:index')
                        else:
                            messages.error(request, 'Type d\'utilisateur non reconnu.')
                            logout(request)
                            return redirect('clients:connexion')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()
    return render(request, 'clients/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('clients:connexion')

def inscription(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            try:
                client = form.save()
                # Log the user in after registration
                login(request, client.user)
                messages.success(request, 'Compte créé avec succès!')
                return redirect('clients:profil', pk=client.pk)
            except Exception as e:
                messages.error(request, f'Erreur lors de la création du compte: {str(e)}')
    else:
        form = ClientRegistrationForm()
    return render(request, 'clients/inscription.html', {'form': form})

def profil(request, pk):
    client = get_object_or_404(Client, pk=pk)
    vehicules = Vehicule.objects.filter(client=client)
    return render(request, 'clients/profil.html', {
        'client': client,
        'vehicules': vehicules
    })

def modifier_profil(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil mis à jour avec succès!')
            return redirect('clients:profil', pk=client.pk)
    else:
        form = ClientUpdateForm(instance=client)
    return render(request, 'clients/modifier_profil.html', {'form': form})

def mes_vehicules(request, pk):
    client = get_object_or_404(Client, pk=pk)
    vehicules = Vehicule.objects.filter(client=client)
    return render(request, 'clients/mes_vehicules.html', {
        'client': client,
        'vehicules': vehicules
    })

def ajouter_vehicule(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = VehiculeForm(request.POST)
        if form.is_valid():
            vehicule = form.save(commit=False)
            vehicule.client = client
            vehicule.save()
            messages.success(request, 'Véhicule ajouté avec succès!')
            return redirect('clients:mes_vehicules', pk=client.pk)
    else:
        form = VehiculeForm()
    return render(request, 'clients/ajouter_vehicule.html', {'form': form})

def details_vehicule(request, pk, vehicule_pk):
    client = get_object_or_404(Client, pk=pk)
    vehicule = get_object_or_404(Vehicule, pk=vehicule_pk, client=client)
    return render(request, 'clients/details_vehicule.html', {'vehicule': vehicule})

def prendre_rendez_vous(request, pk):
    client = get_object_or_404(Client, pk=pk)
    vehicules = Vehicule.objects.filter(client=client)
    if request.method == 'POST':
        # Handle rendez-vous creation
        pass
    return render(request, 'clients/prendre_rendez_vous.html', {'vehicules': vehicules})

#def mes_rendez_vous(request, pk):
    #client = get_object_or_404(Client, pk=pk)
    #rendez_vous = RendezVous.objects.filter(client=client)
    #return render(request, 'clients/mes_rendez_vous.html', {'rendez_vous': rendez_vous})

#def annuler_rendez_vous(request, pk, rendez_vous_pk):
    #client = get_object_or_404(Client, pk=pk)
    #rendez_vous = get_object_or_404(RendezVous, pk=rendez_vous_pk, client=client)
    #if request.method == 'POST':
        #rendez_vous.delete()
        #messages.success(request, 'Rendez-vous annulé avec succès!')
        #return redirect('mes_rendez_vous', pk=client.pk)
    #return render(request, 'clients/annuler_rendez_vous.html', {'rendez_vous': rendez_vous})
