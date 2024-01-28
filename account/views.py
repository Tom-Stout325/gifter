from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import *
from .models import Account
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class RegisterUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = RegisterUpdate
    login_url = 'login'
    template_name = "registration/register_update.html"
    success_url = reverse_lazy('home')
    success_message = "User updated"

    def get_object(self):
        return self.request.user

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Errors")
        return redirect('home')

        
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f'{ user.username} has been logged in.')
                return redirect(f'/my-profile/{user.id}')
            else:
                messages.error(request, 'Account is not active, please contact the administrator')
                return render(request, 'login')
        else:
            messages.success(request, "Invalid login")
    return render(request, 'registration/login.html', {'form': LoginForm})


def logoutView(request):
    logout(request)
    messages.success(request, 'You have logged out.')
    return redirect('home')

