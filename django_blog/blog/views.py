from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import (
    Post, Category
)

from django.views.generic import ListView


def post_detail(request, slug, pk):

    post = get_object_or_404(Post, slug=slug)

    context = {
        'post_detail': post,
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
