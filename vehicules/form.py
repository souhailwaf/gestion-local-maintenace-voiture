from django import forms
from .models import Vehicule

class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['marque', 'immatricule']
        widgets = {
            'immatricule': forms.TextInput(attrs={'placeholder': 'Entrer immatricule du vehicule'}),
        }