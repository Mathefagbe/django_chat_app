from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager,AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.apps import apps





# Create your models here.

class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self,username,email, password, **extra_fields):
        if not username:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username,email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username,email, password, **extra_fields)

    def create_superuser(self,username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username,email, password, **extra_fields)

    
class CustomUsers(AbstractBaseUser,PermissionsMixin):
    full_name=models.CharField(_("Full Name"),max_length=400,null=True)
    username=models.CharField(_("username"),unique=True,max_length=400)
    email=models.EmailField(_("Email Address"),unique=False,)
    is_staff = models.BooleanField(_("staff status"), default=False )
    is_active = models.BooleanField( _("active"),default=True,)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    confirm_password=models.CharField(max_length=100,null=True)


    EMAIL_FIELD = ""
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects=CustomUserManager()


    def __str__(self) -> str:
        return self.username
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


User=get_user_model()

 
class UserProfile(models.Model):
    image=models.ImageField(upload_to='profiles',default="profiles/user1.png")
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')