from django.db import models
from django.contrib.auth.models import User
from PIL import Image




class Family(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatars", default='default_family.png', blank=True, null=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "Families"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

 

class Gift(models.Model):
    user = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    qty = models.IntegerField(default='1')
    image = models.ImageField(default='default_gift.png', upload_to="gifts", blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=100, blank=True, null=True)
    store = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    purchased = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"  

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)



class Hobby(models.Model):
    user = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}" 
    
    class Meta:
        verbose_name_plural = "Hobbies"

