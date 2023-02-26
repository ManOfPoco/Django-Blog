from django.views.generic import ListView

from blog.models import Post, Category


class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_create']
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[:5]
        return context
    
