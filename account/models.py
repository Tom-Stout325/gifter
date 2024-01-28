from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from PIL import Image


class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("A valid email address is required.")
        if not username:
            raise ValueError("A unique username is required.")
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)

class Account(AbstractBaseUser, PermissionsMixin):
    email                   = models.EmailField(max_length=100, unique=True)
    username                = models.CharField(max_length=50, unique=True)
    first_name              = models.CharField(max_length=50)
    last_name               = models.CharField(max_length=50)
    family                  = models.ForeignKey('gifter.Family', on_delete=models.CASCADE, blank=True, null=True)
    birthday                = models.DateField(blank=True, null=True)
    anniversary             = models.DateField(blank=True, null=True)
    date_joined             = models.DateField(verbose_name='Date Joined', auto_now_add=True)
    last_login              = models.DateField(verbose_name='Last Login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    profile_image           = models.ImageField(max_length=255, upload_to='profile_images', null=True, blank=True, default='default_user.png')
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.profile_image.path)