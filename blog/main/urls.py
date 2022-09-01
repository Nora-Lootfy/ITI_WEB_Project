from django.urls import path

from categories.views import get_categories, PostList
from . import views

urlpatterns = [
    path('', PostList.as_view(), name='posts-index'),
    path('', get_categories, name='get-catiegores'),
    path("admin_panel/<int:id>", views.admin_panel, name="admin_panel"),
]
