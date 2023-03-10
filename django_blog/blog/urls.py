from django.urls import path

from .views import (
    post_detail,
    CategoryPostList,
    CategoryList,
    UserPostList,
    CreatePostView,
    DeletePostView,
    UpdatePostView,
    DeleteCommentView
)

from django.views.generic import RedirectView

app_name = 'blog'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home')),
    path('post-detail/<slug:slug>/<int:pk>',
         post_detail, name='blog_detail'),
    path('category/', CategoryList.as_view(), name='categories'),
    path('category/<slug:slug>', CategoryPostList.as_view(), name='category'),
    path('<slug:slug>/posts', UserPostList.as_view(), name='user_posts'),

    path('new-post/', CreatePostView.as_view(), name='new_post'),
    path('delete-post/<slug:slug>/<int:pk>/',
         DeletePostView.as_view(), name='delete_post'),
    path('<slug:slug>/<int:pk>/edit/', UpdatePostView.as_view(), name='edit_post'),
    path('delete-comment/<slug:slug>/<int:pk>/',
         DeleteCommentView.as_view(), name='delete_comment'),
]
