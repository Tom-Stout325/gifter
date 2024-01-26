from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
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



class RegisterUpdate(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = RegisterUpdate
    template_name = 'registration/register_update.html'
    success_url = reverse_lazy('myProfile')

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        update = super().get_context_data(**kwargs)
        update['account'] = Account.objects.filter(account=self.get_object().pk)
        return update




# @login_required(login_url='login')
# def registerUpdate(request, pk):
#     user = Account.objects.get(id=pk)
#     if request.method == 'POST':
#         form = RegisterUpdate(request.POST, instance=request.user)
       
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('myProfile')
#     else:
#         form = RegisterUpdate(instance=request.user)

#     context = {
#         'form': form,
   
#     }
  
#     return render(request, 'registration/register_update.html', context)




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









def account_view(request, *args, **kwargs):
	context = {}
	user_id = kwargs.get("user_id")
	try:
		account = Account.objects.get(pk=user_id)
	except:
		return HttpResponse("No user found.")
	if account:
		context['id'] = account.id
		context['username'] = account.username
		context['email'] = account.email
		context['profile_image'] = account.profile_image.url
			
		return render(request, "account/account.html", context)