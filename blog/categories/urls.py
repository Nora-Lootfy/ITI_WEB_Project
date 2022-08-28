from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate

urlpatterns = [
    path('posts/', PostList.as_view(), name='posts-index'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post-details'),
    path('createpost', PostCreate.as_view(), name='create-post'),
    path('editpost/<int:pk>', PostUpdate.as_view(), name='edit-post'),
]
