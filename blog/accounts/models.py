from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserModel(User):
    
    @classmethod
    def get_all_admins(cls):
        return User.objects.filter(is_staff=True)
    

    @classmethod
    def get_active_admin(cls):
        return User.objects.filter(is_staff=True, is_active=True)
    
    @classmethod
    def get_all_users(cls):
        return User.objects.all()
    
    def get_admin_url(self):
        return reverse("admin_panel", self.id)