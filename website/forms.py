from django import forms
from .models import *


# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ('birthday', 'anniversary', 'family_name', 'avatar')

#         widgets = {
#             'birthday': forms.DateField(attrs={'class': 'form-control', 'placeholder': 'Enter your birthday'}),
#             'anniversary': forms.DateField(attrs={'class': 'form-control', 'placeholder': 'Enter your anniversary (Not Required).'}),
#             'family_name': forms.CharField(attrs={'class': 'form-control', 'placeholder': 'Family Name'}),
#             'avatar': forms.ImageField()
#         }