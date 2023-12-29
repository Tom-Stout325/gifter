from django.db import models
from django.contrib.auth.models import User



class Family(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default='media/avatars/default_family.png')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "Families"



class Gift(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    store = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)



class Hobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=500)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "Hobbies"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    family_name = models.ForeignKey(Family, on_delete=models.DO_NOTHING)
    birthday = models.DateField(auto_now_add=False, blank=True, null=True)
    anniversary = models.DateField(auto_now_add=False, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='media/avatars/default_user.png')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} {self.user.first_name}" + f"{self.family_name}"
    
    class Meta:
        verbose_name_plural = "Profiles"
    


