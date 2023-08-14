from django import forms
from django.forms import ModelForm
from .models import BaseIntro

class Blog(forms.ModelForm):
    class Meta:
        model = BaseIntro
        fields = "__all__"

