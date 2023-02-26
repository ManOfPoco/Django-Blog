from django.urls import path

from .views import (
    post_detail
)

from django.views.generic import RedirectView

app_name = 'blog'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home')),
    path('post-detail/<slug:slug>/<int:pk>',
         post_detail, name='blog_detail'),
]
