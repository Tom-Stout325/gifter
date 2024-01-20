from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages
from django.utils.decorators import method_decorator
from .models import *
from account.models import *
from .forms import *
from account.models import *
from django.contrib.auth import update_session_auth_hash
from django.views import View




class Profiles(ListView):
    model = Account
    template_name = 'gifter/profiles.html'
    context_object_name = 'profiles'


def profile(request, pk):
    user = Account.objects.get(id=pk)
    gifts = Gift.objects.filter(user__id=pk)
    giftDtl = Gift.objects.filter(id=pk)
    hobby = Hobby.objects.filter(user_id=pk)
    context = {
        'user': user,
        'gifts': gifts,
        'hobby': hobby,
        'giftDtl': giftDtl,
    }
    
    return render(request, 'gifter/profile.html', context)


@login_required(login_url='login')
def myProfile(request, pk):
    account = request.user
    user = Account.objects.get(id=pk)
    gifts = Gift.objects.filter(user_id=pk)
    hobbies = Hobby.objects.filter(user_id=pk)
    context = {
        'user': user,
        'gifts': gifts,
        'hobbies': hobbies,
        'account': account,
    }
    print(user)
    return render(request, 'gifter/myProfile.html', context)


class Families(ListView):
    model = Family
    template_name = 'gifter/families.html'
    context_object_name = 'family'


def family(request, pk):
    family = Family.objects.filter(id = pk)
    users = Account.objects.filter(family_id=pk)
    context = {
        'family': family,
        'users': users,
    }
    return render(request, 'gifter/family.html', context)






def giftDetail(request, pk):
    gift = Gift.objects.get(id=pk)
    context = {  
        'gift': gift,
       
     
    }
    print(gift)
    return render(request, 'gifter/gift_detail.html', context)




def giftAdd(request):
    form = GiftForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, ('Gift has been added'))
        return redirect('myProfile')
    context = {
        'form': form,
    }
    return render(request, 'components/giftAdd.html', context)



def giftUpdate(request, pk):
    pass





def hobbies(request):
    pass



def AboutPage(request):
    return render(request,'gifter/about.html')

def ContactPage(request):
    return render(request,'gifter/contact.html')

def HomePage(request):
    return render(request,'gifter/home.html')


#=-=-=-=-=-=-=-=-=-=-=-=-=->  NOT USED <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


