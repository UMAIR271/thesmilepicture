from statistics import mode
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from .models import Smile , profile


class smileSubmitForm (ModelForm):
    class Meta:
        model = Smile
        fields = '__all__'
        widgets = {
            'smileReason': forms.TextInput(attrs={'class': 'form-control'}),
            'smileUserName': forms.TextInput(attrs={'class': 'form-control'}),
        }


class profilrSubmitForm (ModelForm):
    class Meta:
        model = profile
        fields = '__all__'
