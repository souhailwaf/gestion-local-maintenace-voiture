from django import forms
from .models import Reparation
class ReparationForm(forms.ModelForm):
    class Meta:
        model = Reparation
        fields =['mecanicien','vehicule','date_debut','date_fin','description','etat','cout']
    
