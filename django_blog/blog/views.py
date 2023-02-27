from django.shortcuts import (
    get_list_or_404, get_object_or_404,
    render, redirect
)
from django.urls import reverse

from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Category, PostComment
from users.models import Profile

from .forms import CreatePostForm, PostCommentForm


def post_detail(request, slug, pk):

    if request.POST:
        if request.user.is_authenticated:

            post = Post.objects.get(slug=slug, id=pk)

            if 'comment' in request.POST:
                comment_form = PostCommentForm(request.POST)

                if comment_form.is_valid():

                    comment_form.instance.author = request.user
                    comment_form.instance.post = post

                    comment_form.save()

            return redirect(post.get_absolute_url())

        else:
            return redirect('/users/sign-in/')

    else:

        post = get_object_or_404(Post, slug=slug)
        comments = PostComment.objects.filter(
            post=post).order_by('-date_create')

        context = {
            'post_detail': post,
            'comments': comments,
            'comment_form': PostCommentForm(),
        }

        return render(request, 'blog/post_detail.html', context=context)


class CategoryList(ListView):
    model = Category
    template_name = 'blog/category.html'
    context_object_name = 'categories'

    def get_queryset(self):
        if self.kwargs.get('slug'):
            query_set = get_list_or_404(
                Post.objects.filter(
                    category=get_object_or_404(
                        Category, slug=self.kwargs['slug'])))
        else:
            query_set = Post.objects.all().order_by('-date_create')
        return query_set


class UserPostList(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'user_posts'

    def get_queryset(self):
        queryset = Post.objects.filter(
            author=Profile.objects.get(
                slug=self.kwargs['slug']).user).order_by('-date_create')
        return queryset


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'blog/post_create_form.html'

    def form_valid(self, form: CreatePostForm):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/post_create_form.html'


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
