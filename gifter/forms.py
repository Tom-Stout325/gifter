from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *



class GiftForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}),required=False)
    color = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    size = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    store = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),required=False)
    
    class Meta:
        model = Gift
        fields = ['name', 'qty', 'image', 'color', 'size', 'store', 'description']



class HobbyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Hobby
        fields = ['name', 'description']
