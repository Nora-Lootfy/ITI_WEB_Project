from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, likeview, dislikeview, PostDelete, subscribe, undislikeview, unlikeview, ussubscribe

urlpatterns = [
    path('posts/<int:pk>', PostDetail.as_view(), name='post-details'),
    path('createpost', PostCreate.as_view(), name='create-post'),
    path('editpost/<int:pk>', PostUpdate.as_view(), name='edit-post'),
    path('like/<int:pk>', likeview, name="like-post"),
    path('dislike/<int:pk>', dislikeview, name='dislike-post'),
    path('unlike/<int:pk>', unlikeview, name="unlike-post"),
    path('undislike/<int:pk>', undislikeview, name='undislike-post'),
    path('deletepost/<int:pk>', PostDelete.as_view(), name='delete-post'),
    path('subscribe/<int:pk>', subscribe, name="subscribe-category"),
    path('unsbscribe/<int:pk>', ussubscribe, name='unsubscribe-category')
]
