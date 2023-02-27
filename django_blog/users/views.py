from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from django.core.paginator import Paginator

from .models import Profile, Follow
from blog.models import Post

from django.views.generic import TemplateView, CreateView

from .forms import (
    ProfileUpdateForm, UserUpdateForm,
    MyUserCreationForm,
)

from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/sign-up.html'
    success_url = reverse_lazy('users:sign-in')

    def form_valid(self, form: MyUserCreationForm):
        form.save()
        return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = get_object_or_404(Profile, slug=self.kwargs['slug'])
        context["profile"] = profile

        post = Post.objects.filter(
            author=profile.user).order_by('-date_create')[:3]
        context["post"] = post

        return context

    def post(self, request, *args, **kwargs):
        follow_system(request, *args, **kwargs)

        return redirect('users:profile', slug=kwargs['slug'])


def follow_system(request, *args, **kwargs):

    option = request.POST['option']
    user_slug = request.POST['user']

    user = get_object_or_404(Profile, slug=user_slug).user
    if option == 'follow':
        Follow.objects.create(
            follower=request.user, following=user)
    elif option == 'unfollow':
        get_object_or_404(
            Follow, follower=request.user, following=user).delete()

    return redirect('users:profile', slug=kwargs['slug'])


@login_required(login_url='/users/sign-in/')
def profile_settings(request):

    if request.method == 'POST':
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()

            return redirect(reverse('users:settings'))
    else:
        profile_form = ProfileUpdateForm(
            instance=request.user.profile)
        user_form = UserUpdateForm(
            instance=request.user)

    context = {
        'profile_form': profile_form,
        'user_form': user_form
    }
    return render(request, 'users/settings.html', context)


class FollowersFollowingView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = get_object_or_404(Profile, slug=kwargs['slug'])

        if self.request.path == reverse('users:followers_list', kwargs=kwargs):
            context["followers_list"] = profile.followers_list
            context["followers_count"] = profile.followers_count
            paginator = Paginator(profile.followers_list, 10)

        else:
            context["following_list"] = profile.following_list
            context["following_count"] = profile.following_count
            paginator = Paginator(profile.following_list, 10)

        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['paginator'] = paginator

        return context

    def post(self, request, *args, **kwargs):
        follow_system(request, *args, **kwargs)

        if request.path == reverse('users:followers_list', kwargs=kwargs):
            return redirect('users:followers_list', slug=kwargs['slug'])
        else:
            return redirect('users:following_list', slug=kwargs['slug'])

    def get_template_names(self):
        slug = get_object_or_404(
            Profile, slug=self.request.path.split('/')[2]).slug

        if self.request.path == reverse('users:following_list',
                                        kwargs={'slug': slug}):
            return 'users/following.html'
        else:
            return 'users/followers.html'
