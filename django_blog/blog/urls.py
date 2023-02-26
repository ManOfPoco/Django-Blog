from django.urls import path

from .views import (
    post_detail,
    CategoryList,
    UserPostList
)

from django.views.generic import RedirectView

app_name = 'blog'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home')),
    path('post-detail/<slug:slug>/<int:pk>',
         post_detail, name='blog_detail'),
    path('category/', CategoryList.as_view(), name='categories'),
    path('category/<slug:slug>', CategoryList.as_view(), name='category'),
    path('<slug:slug>/posts', UserPostList.as_view(), name='user_posts'),
]
