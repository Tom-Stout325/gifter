from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Account
from django.contrib.auth.models import User


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



def registerUpdate(request, pk):
    user = Account.objects.get(id=pk)

    if request.method == 'POST':
        form = RegisterUpdate(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile has been updated.')
            context = {
                'form': form,
            }
            return redirect('myProfile', context)
    else:
        form = RegisterUpdate(request.POST, request.FILES, instance=request.user)
        context = {
                'form': form,
            }
        return render(request, 'registration/register_update.html', context)


class RegisterUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = RegisterUpdate
    login_url = 'login'
    template_name = "registration/register_update.html"
    success_url = reverse_lazy('myProfile')
    success_message = "User updated"

    def get_object(self):
        return self.request.user

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Errors")
        return redirect('myProfile')

        
	


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login')
    return render(request, 'registration/login.html', {'form': LoginForm})


def logoutView(request):
	logout(request)
	return redirect("home")

