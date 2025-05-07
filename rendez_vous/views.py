from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import RendezVous
from .form import RendezVousForm

@login_required
def prendre_rendez_vous(request):
    if not hasattr(request.user, 'client'):
        messages.error(request, 'Vous devez être un client pour prendre rendez-vous.')
        return redirect('home')

    if request.method == 'POST':
        form = RendezVousForm(request.POST, client=request.user.client)
        if form.is_valid():
            rendez_vous = form.save(commit=False)
            rendez_vous.client = request.user.client
            rendez_vous.save()
            messages.success(request, 'Votre rendez-vous a été enregistré avec succès!')
            return redirect('rendez_vous:mes_rendez_vous')
    else:
        form = RendezVousForm(client=request.user.client)

    return render(request, 'rendez_vous/prendre_rendez_vous.html', {'form': form})

@login_required
def mes_rendez_vous(request):
    if not hasattr(request.user, 'client'):
        messages.error(request, 'Vous devez être un client pour voir vos rendez-vous.')
        return redirect('home')

    rendez_vous = RendezVous.objects.filter(client=request.user.client).order_by('-date_heure')
    return render(request, 'rendez_vous/mes_rendez_vous.html', {'rendez_vous': rendez_vous})

@login_required
def annuler_rendez_vous(request, pk):
    if not hasattr(request.user, 'client'):
        messages.error(request, 'Vous devez être un client pour annuler un rendez-vous.')
        return redirect('home')

    rendez_vous = get_object_or_404(RendezVous, pk=pk, client=request.user.client)
    
    if request.method == 'POST':
        rendez_vous.status = 'annule'
        rendez_vous.save()
        messages.success(request, 'Le rendez-vous a été annulé avec succès.')
        return redirect('rendez_vous:mes_rendez_vous')
    
    return render(request, 'rendez_vous/annuler_rendez_vous.html', {'rendez_vous': rendez_vous})

