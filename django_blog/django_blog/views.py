from django.shortcuts import render

from blog.models import Post, Category
from django.views.generic import ListView


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-last_updated', '-category']
    paginate_by = 10
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[:5]
        return context
