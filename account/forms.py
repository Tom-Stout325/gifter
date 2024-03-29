from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from gifter.models import *
from .models import *



class RegisterForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	family = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Family.objects.all())
	birthday = forms.DateField(widget=forms.DateInput(attrs={'class':'form-content', 'type':'date', 'input_type': 'text'}))
	anniversary = forms.DateField(widget=forms.DateInput(attrs={'class':'form-content', 'type':'date'}), required=False)
	profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    
	class Meta:
		model = Account
		fields = ('email', 'username', 'first_name', 'last_name', 'family', 'birthday', 'anniversary', 'profile_image', 'password1', 'password2', )


class RegisterUpdate(forms.ModelForm):
	password = None
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),required=False)
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
	family = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Family.objects.all(),required=False)
	birthday = forms.DateField(widget=forms.DateInput(attrs={'class':'form-content', 'type':'date'}),required=False)
	anniversary = forms.DateField(widget=forms.DateInput(attrs={'class':'form-content', 'type':'date'}),required=False)
	profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}),required=False)

	class Meta:
		model = Account
		fields = ('email', 'username', 'first_name', 'last_name', 'family', 'birthday', 'anniversary', 'profile_image' )
			
	def __init__(self, *args, **kwargs):
		super(RegisterUpdate, self).__init__(*args, **kwargs)


class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))

	class Meta:
		model = Account
		fields = ('username', 'password')