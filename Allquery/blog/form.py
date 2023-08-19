from django import forms
from django.forms import ModelForm
from .models import *

class Blog(forms.ModelForm):
    class Meta:
        model = BaseIntro
        fields = "__all__"


class AboutForm(forms.ModelForm):
    class Meta:
        model = RingTone  
        filter  =  "customer"
        fields = "__all__"

