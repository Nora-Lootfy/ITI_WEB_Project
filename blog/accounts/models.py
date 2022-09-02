from django.shortcuts import reverse, get_object_or_404
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserModel(User):
    @classmethod
    def get_all_admins(cls):
        return cls.objects.filter(is_staff=True)

    @classmethod
    def get_active_admin(cls):
        return cls.objects.filter(is_active=True)

    @classmethod
    def get_all_users(cls):
        return cls.objects.all()

    def get_admin_url(self):
        return reverse("admin_panel", self.id)
    
    @classmethod
    def get_user_by_id(cls, id):
        return get_object_or_404(cls, pk=id)
