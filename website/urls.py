from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('about', AboutPage, name='about'),
    path('contact', ContactPage, name='contact'),
    path('', HomePage, name='home'),
    path('families/', AllFamilyView.as_view(), name='families'),
    path('family/<str:pk>/', familyProfiles, name='family'),
    path('profile/', MyProfile.as_view(), name='profile'),
    path('profile_dtl/<str:pk>/', profileDtl, name='profile_dtl'),
    path('profiles/', AllProfiles.as_view(), name='profiles'),
    

    
]
