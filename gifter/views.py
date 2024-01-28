from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import Account
from .models import *
from .forms import *


#=-=-=-=-=-=-=-=-=-=-=-=-=->  P R O F I L E   V I E W S  <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

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
    return render(request, 'gifter/myProfile.html', context)


#=-=-=-=-=-=-=-=-=-=-=-=-=->  F A M I L Y   V I E W S  <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

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


#=-=-=-=-=-=-=-=-=-=-=-=-=->  G I F T  V I E W S  <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

@login_required(login_url='login')
def addGift(request):
    if request.method == 'POST':
        form = GiftForm(request.POST)
        if form.is_valid():
            gift = form.save(commit=False)
            gift.user = request.user
            gift.save()
            return redirect(f'/my-profile/{gift.user_id}')
    else:
        form = GiftForm()
    return render(request, 'components/gift_add.html', {"form": form})


def giftDetail(request, pk):
    gift = Gift.objects.get(id=pk)
    context = {  
        'gift': gift,
    }
    return render(request, 'components/gift_detail.html', context)


@login_required(login_url='login')
def giftUpdate(request, pk):
    gift = Gift.objects.get(id=pk)
    form = GiftForm(instance=gift)
    context = {
            'form': form,
            'gift': gift,
        }
    if request.method == 'POST':
        form = GiftForm(request.POST, request.FILES, instance=gift)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your hobby has been updated') 
            return redirect(f'/my-profile/{gift.user_id}')
   
        return render(request, 'components/gift_update.html', context)
    return render(request, 'components/gift_update.html', context)


@login_required(login_url='login')
def deleteGift(request, pk):
    gift = Gift.objects.get(id=pk)
    if request.method == 'POST':
        gift.delete()
        messages.success(request, f'Successfully deleted from your Wish List.') 
        return redirect(f'/my-profile/{gift.user_id}')
    context = {
        'gift': gift,
     }

    return render(request, 'components/gift_delete.html', context)


#=-=-=-=-=-=-=-=-=-=-=-=-=->  H O B B Y  V I E W S  <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

@login_required(login_url='login')
def addHobby(request):
    if request.method == 'POST':
        form = HobbyForm(request.POST)
        if form.is_valid():
            hobby = form.save(commit=False)
            hobby.user = request.user
            hobby.save()
            return redirect(f'/my-profile/{hobby.user_id}')
    else:
       
        form = HobbyForm()
    return render(request, 'components/hobby_add.html', {"form": form})


def hobbyDetail(request, pk):
    hobby = Hobby.objects.get(id=pk)
    context = {  
        'hobby': hobby,
    }
    return render(request, 'components/hobby_detail.html', context)


@login_required(login_url='login')
def hobbyUpdate(request, pk):
    hobby = Hobby.objects.get(id=pk)
    form = HobbyForm(instance=hobby)
    context = {
        'form': form,
        'hobby': hobby, 
        }
    if request.method == 'POST':
        form = HobbyForm(request.POST, instance = hobby)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your hobby has been updated') 
            return redirect(f'/my-profile/{hobby.user_id}')

        return render(request, 'components/hobby_update.html', context)
    return render(request, 'components/hobby_update.html', context)


@login_required(login_url='login')
def deleteHobby(request, pk):
    hobby = Hobby.objects.get(id=pk)
    if request.method == 'POST':
        hobby.delete()
        messages.success(request, 'Your hobby was deleted successfully.') 
        return redirect(f'/my-profile/{hobby.user_id}')
    context = {
        'hobby': hobby,
     }
    return render(request, 'components/hobby_delete.html', context)
    




#=-=-=-=-=-=-=-=-=-=-=-=-=-> P A G E   V I E W S <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

def AboutPage(request):
    return render(request,'gifter/about.html')

def ContactPage(request):
    return render(request,'gifter/contact.html')

def HomePage(request):
    return render(request,'gifter/home.html')




