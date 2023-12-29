from django.contrib import admin
from .models import *



class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
   
   
class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Family, FamilyAdmin)

admin.site.register(Profile, ProfileAdmin)