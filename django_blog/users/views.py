from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from django.core.paginator import Paginator

from django.views.generic import CreateView, TemplateView

from .forms import (
    MyUserCreationForm,
)

from .models import Profile
from blog.models import Post



class SignUpView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/sign-up.html'
    success_url = reverse_lazy('users:sign-in')

    def form_valid(self, form: MyUserCreationForm):
        form.save()
        return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def test_func(self):
        return self.request.user.is_authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = get_object_or_404(Profile, slug=self.kwargs['slug'])
        context["profile"] = profile

        post = Post.objects.filter(
            author=profile.user).order_by('-date_create')[:3]
        context["post"] = post

        return context
