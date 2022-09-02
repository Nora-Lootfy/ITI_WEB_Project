from django.urls import path

from categories.views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path("admin_panel/<int:id>", views.admin_panel, name="admin_panel"),
    path("admin_panel/users", views.make_admin, name="make_admin"),
]
