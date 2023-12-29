from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from .models import *
from accounts.models import *



def AboutPage(request):
    return render(request,'website/about.html')

def ContactPage(request):
    return render(request,'website/contact.html')

def HomePage(request):
    return render(request,'website/home.html')


class AllFamilyView(ListView):
    model = Family
    template_name = 'website/families.html'
    context_object_name = 'family'


def familyProfiles(request, pk):
    profiles = Profile.objects.filter(family_name_id = pk)
    context = {
        'profiles': profiles,
    }
    return render(request, 'website/family.html', context)


class AllProfiles(ListView):
    model = Profile
    template_name = 'website/profiles.html'
    context_object_name = 'profiles'


class MyProfile(DetailView):
    model = Profile
    template_name = 'website/profile_my.html'
    context_object_name = 'profile'


def profileDtl(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {
        'profile': profile
    }
    return render(request, 'website/profiles_detail.html', context)


    









class CreateProfile(CreateView):
    model = Profile



