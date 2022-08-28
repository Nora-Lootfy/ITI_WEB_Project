from re import template
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('register/', views.register, name='register'),
     path('logout/', auth_views.LogoutView.as_view(), name="logout"),
     path('login/', auth_views.LoginView
          .as_view(template_name="accounts/login.html"), name="login"),
     path('changepassword', auth_views.PasswordChangeView.as_view(template_name="accounts/changepassword.html"),
          name='change_password'),
     path('changepassword/done', auth_views.PasswordChangeDoneView.as_view(template_name="accounts/changepassworddone.html"),
          name='password_change_done'),
]