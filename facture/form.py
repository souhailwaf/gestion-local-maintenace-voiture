from django import forms
from .models import Facture

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['client','vehicule','total']


class FactureUpdateForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['client','vehicule','total']
        
        