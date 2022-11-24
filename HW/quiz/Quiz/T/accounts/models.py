from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from . managers import UserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    phone_number = models.CharField(max_length=11 , unique=True)
    full_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email','full_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    def  is_staff(self):
        return self.is_admin

#____________________
class OptCode(models.Model):
    phone_number= models.CharField(max_length=11,unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'