from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BuyerForm(forms.ModelForm):
    name=forms.CharField(max_length=50)
    #surname=
    email=forms.EmailField()

    class Meta:
        model = Buyer
        exclude = {""}