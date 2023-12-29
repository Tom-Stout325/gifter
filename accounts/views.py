from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .models import *
from .forms import *





def register(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('first_name')
        messages.success(request, 'Acccount successfully created for ' + user)
        return redirect('login')

    context = { 
        'form': form
    } 
    return render (request, 'registration/register.html', context)




def loginPage (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, username)
            redirect('home')
    context = {} 
    return render (request, 'registration/login.htmI', context)




def logout_view(request):
    logout(request)
    messages.success('Thank you for Signing Out out.')
    return redirect('home')