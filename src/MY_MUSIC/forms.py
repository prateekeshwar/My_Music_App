from django import forms
from .models import Album,Songs
from django.contrib.auth.models import User
class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields=[
            "album_title",
            "artist",
            "genre",
            "album_logo",
            ]
            
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class SongsForm(forms.ModelForm):
    class Meta:
        model=Songs
        fields=[
            "album",
            "song_title",
            "audio_file",
            "is_favourite",
             "album_logo",
            ]