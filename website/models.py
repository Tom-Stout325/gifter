from django.db import models
from django.contrib.auth.models import User



class Family(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default='media/avatars/default_family.png')

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "Families"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    family_name = models.ForeignKey(Family, on_delete=models.DO_NOTHING)
    birthday = models.DateField(blank=True, null=True)
    anniversary = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='media/avatars/default_user.png')

    def __str__(self):
        return f"{self.user.username} {self.user.first_name}" + f"{self.family_name}"
    
    class Meta:
        verbose_name_plural = "Profiles"
    


