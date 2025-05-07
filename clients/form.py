from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from .models import Client

class ClientRegistrationForm(UserCreationForm):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100)
    telephone = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)
    adresse = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nom', 'prenom', 'telephone', 'email', 'adresse']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            client = Client.objects.create(
                user=user,
                nom=self.cleaned_data['nom'],
                prenom=self.cleaned_data['prenom'],
                telephone=self.cleaned_data['telephone'],
                email=self.cleaned_data['email'],
                adresse=self.cleaned_data['adresse']
            )
        return client

class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'telephone', 'email', 'adresse']
        widgets = {
            'adresse': forms.Textarea(attrs={'rows': 3}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@email.com'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        }
        