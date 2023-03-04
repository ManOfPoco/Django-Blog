from django.shortcuts import render
from django.views.decorators.http import require_GET

from django.core.paginator import Paginator

from blog.models import Post, Category
from django.contrib.auth.models import User
from django.db.models import Q


@require_GET
def search(request):
    query = request.GET.get('query')

    search_types = {
        'post': {'search': Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)),
            'template_name': 'posts.html'},
        'people': {'search': User.objects.select_related('profile').filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)), 'template_name': 'people.html'},
        'category': {'search': Category.objects.filter(
            Q(name__icontains=query)), 'template_name': 'category.html'},
    }

    if 'search_for' in request.GET:
        search_for = request.GET.get('search_for')
    else:
        search_for = 'post'

    search_data, template_name = search_types[search_for].values()

    paginator = Paginator(search_data, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template_name = f'search/{template_name}'
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, template_name, context)
