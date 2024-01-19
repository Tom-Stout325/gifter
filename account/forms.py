from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class RegisterForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    
	class Meta:
		model = Account
		fields = ('email', 'username', 'first_name', 'last_name', 'profile_image', 'password1', 'password2', )



class RegisterUpdate(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	profile_image  = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

	class Meta:
		model = Account
		fields = ('email', 'username', 'first_name', 'last_name', 'profile_image')
			

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))

	class Meta:
		model = Account
		fields = ('username', 'password')