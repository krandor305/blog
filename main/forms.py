from .models import Article
from django import forms
from django.forms import ModelForm

class AjoutarticleForm(ModelForm):
    class Meta:
        model = Article
        exclude=['utilisateur']