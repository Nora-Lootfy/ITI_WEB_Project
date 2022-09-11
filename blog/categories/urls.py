from django.urls import path
from .views import PostDetail, PostCreate, PostUpdate, likeview, dislikeview, PostDelete, subscribe, undislikeview, unlikeview, ussubscribe, CategoryCreate, ForbiddenWordCreate, ForbiddenWordUpdate, CategoryDelete, ForbiddenWordDelete, CategoryUpdate

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
    path('unsbscribe/<int:pk>', ussubscribe, name='unsubscribe-category'),
    path('create_category/', CategoryCreate.as_view(), name="create-category"),
    path('create_forbidden_word/', ForbiddenWordCreate.as_view(),
         name="create-forbidden-word"),
    path('update_category/<int:pk>',
         CategoryUpdate.as_view(), name="update-category"),
    path('update_forbidden_word/<int:pk>',
         ForbiddenWordUpdate.as_view(), name="update-forbidden-word"),
    path('delete_category/<int:pk>',
         CategoryDelete.as_view(), name="delete-category"),
    path('delete_forbidden_word/<int:pk>',
         ForbiddenWordDelete.as_view(), name="delete-forbidden-word"),
]
