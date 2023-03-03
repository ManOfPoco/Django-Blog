from django.shortcuts import (
    get_list_or_404, get_object_or_404,
    render, redirect
)
from django.urls import reverse

from django.views.generic import (
    ListView, CreateView, DeleteView, UpdateView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Category, PostComment, PostLike
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

                    if 'parent' in request.POST:
                        parent = PostComment.objects.get(
                            id=request.POST.get('parent'))

                        comment_form.instance.parent = parent

                    comment_form.save()

            elif 'like_post' in request.POST:

                if request.POST.get('option') == 'Unlike':
                    get_object_or_404(PostLike,
                                      post=post, author=request.user).delete()

                elif request.POST.get('option') == 'Like':
                    PostLike.objects.create(
                        post=post, author=request.user)

            return redirect(post.get_absolute_url())

        else:
            return redirect('/users/sign-in/')

    else:

        post = get_object_or_404(Post, slug=slug, id=pk)
        comments = PostComment.objects.filter(
            post=post)

        context = {
            'post_detail': post,
            'comments': comments,
            'comment_form': PostCommentForm(),
        }
        if request.user.is_authenticated:
            context['is_liked'] = post.likes.filter(
                author=request.user).exists()

        return render(request, 'blog/post_detail.html', context=context)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = PostComment

    def get_success_url(self) -> str:
        comment = self.get_object()
        return reverse('blog:blog_detail', kwargs={
            'slug': comment.post.slug,
            'pk': comment.post.id
        })


class UserPostList(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.filter(
            author=Profile.objects.get(
                slug=self.kwargs['slug']).user).order_by('-date_create')
        return queryset


class CategoryPostList(ListView):
    model = Category
    template_name = 'blog/category.html'
    paginate_by = 10

    def get_queryset(self):
        if self.kwargs.get('slug'):
            query_set = Post.objects.filter(
                category=get_object_or_404(
                    Category, slug=self.kwargs['slug']))
            return query_set


class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'


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
    template_name = 'blog/post_form.html'
