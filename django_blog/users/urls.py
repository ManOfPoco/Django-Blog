from django.urls import path
from . import views

from django.views.generic import RedirectView


app_name = 'users'


urlpatterns = [
    path('', RedirectView.as_view(url='/')),
]
