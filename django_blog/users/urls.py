from django.urls import path
from . import views

from django.views.generic import RedirectView

from .forms import UserAuthenticationForm
import django.contrib.auth.views as auth_views


app_name = 'users'


urlpatterns = [
    path('', RedirectView.as_view(url='/')),

    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('sign-in/', auth_views.LoginView.as_view(
        template_name='registration/sign-in.html',
        form_class=UserAuthenticationForm,
    ), name='sign-in'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('<slug:slug>/profile', views.ProfileView.as_view(), name='profile'),
    path('settings/', views.profile_settings, name='settings'),
    path('<slug:slug>/followers_list/',
         views.FollowersFollowingView.as_view(), name='followers_list'),
    path('<slug:slug>/following_list/',
         views.FollowersFollowingView.as_view(), name='following_list'),
]
