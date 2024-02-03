from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('about/', AboutPage, name='about'),
    path('contact/', ContactPage, name='contact'),
    path('', HomePage, name='home'),

    path('profiles/', Profiles.as_view(), name='profiles'),
    path('profile/<str:pk>/', profile, name='profile'),
    path('my-profile/<str:pk>/', myProfile, name='myProfile'),

    path('families/', Families.as_view(), name='families'),
    path('family/<str:pk>/', family, name='family'),
   
    path('gift/<str:pk>/', giftDetail, name='giftDetail'),
    path('add-gift', addGift, name='addGift'),
    path('update-gift/<str:pk>', giftUpdate, name='giftUpdate'),
    path('delete-gift/<str:pk>/', deleteGift, name='giftDelete'),

    path('parents/', ParentList.as_view(), name='parentList'),
    path('parents/<str:pk>/', listDetail, name='listDetail'),
    path('parent-gift-detail/<str:pk>/', parentGiftDetail, name='parentGiftDetail'),

    path('hobby/<str:pk>/', hobbyDetail, name='hobbyDetail'),
    path('add-hobby/', addHobby, name='addHobby'),
    path('update-hobby/<str:pk>', hobbyUpdate, name='hobbyUpdate'),
    path('delete-hobby/<str:pk>/', deleteHobby, name='hobbyDelete'),

    
]
