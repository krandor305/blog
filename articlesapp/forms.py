from .models import Paragraph
from django import forms
from django.forms import ModelForm

class AjoutparagrapheForm(ModelForm):
    class Meta:
        model = Paragraph
        exclude=['article']