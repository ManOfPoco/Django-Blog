from django.shortcuts import render

from django.core.paginator import Paginator

from django.views.decorators.http import require_GET

from blog.models import Post
from django.db.models import Q


@require_GET
def search(request):
    query = request.GET.get('query')

    search_data = Post.objects.filter(
        Q(title__icontains=query) | Q(body__icontains=query)
    )

    paginator = Paginator(search_data, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, 'search/search.html', context)
