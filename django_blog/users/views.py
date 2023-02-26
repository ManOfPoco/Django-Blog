from django.shortcuts import render
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.views.generic import CreateView

from .forms import (
    MyUserCreationForm,
)


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/sign-up.html'
    success_url = reverse_lazy('users:sign-in')

    def form_valid(self, form: MyUserCreationForm):
        form.save()
        return super().form_valid(form)
