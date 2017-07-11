# Arquivo: apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import MyUser, IdeaTrack


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'spotify_username', 'email']


class TrackForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Nome")
    artist = forms.CharField(max_length=128, help_text="Artista")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = IdeaTrack
        fields = ['name', 'artist']
        exclude = ('user',)
