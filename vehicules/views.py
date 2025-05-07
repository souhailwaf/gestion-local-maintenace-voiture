from django.shortcuts import render, get_object_or_404
from vehicules.models import Vehicule

def vehicule_list(request):
    vehicules = Vehicule.objects.all()
    return render(request, 'vehicules/vehicule_list.html', {'vehicules': vehicules})

def vehicule_detail(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)
    return render(request, 'vehicules/vehicule_details.html', {'vehicule': vehicule})


