from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *




class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name',  'password1', 'password2']



# class RegisterUpdate(forms.ModelForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ['email', 'username', 'first_name', 'last_name']


class RegisterUpdate(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))


class GiftForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    color = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    size = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    store = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Gift
        fields = ['name', 'qty', 'image', 'color', 'size', 'store', 'description']


class HobbyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Hobby
        fields = ['name', 'description']
