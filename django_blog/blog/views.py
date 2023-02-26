from django.shortcuts import render, get_object_or_404

from .models import (
    Post,
)


def post_detail(request, slug, pk):

    post = get_object_or_404(Post, slug=slug)

    context = {
        'post_detail': post,
    }

    return render(request, 'blog/post_detail.html', context=context)
