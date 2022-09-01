from django.urls import path

from categories.views import PostList
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path("admin_panel/<int:id>", views.admin_panel, name="admin_panel"),
]
