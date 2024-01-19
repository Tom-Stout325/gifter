from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('about/', AboutPage, name='about'),
    path('contact/', ContactPage, name='contact'),
    path('home/', HomePage, name='home'),

    path('profiles/', Profiles.as_view(), name='profiles'),
    path('profile/<str:pk>/', profile, name='profile'),
    path('my-profile/<str:pk>/', myProfile, name='myprofile'),

    path('families/', Families.as_view(), name='families'),
    path('family/<str:pk>/', family, name='family'),
   

    path('gift/<str:pk>/', giftDetail, name='giftDetail'),

    
]
