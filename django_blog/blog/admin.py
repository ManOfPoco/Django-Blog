from django.contrib import admin
from .models import Post, Category, PostComment, PostLike



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_create', 'last_updated']

    fields = ['title', 'slug', 'body', 'author', 'category']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('category',)

    list_filter = ['author', 'category', 'date_create', 'last_updated']

    search_fields = ['title', 'author__username']


class CategoryNameFilter(admin.SimpleListFilter):
    title = 'Name'
    parameter_name = 'name'

    def lookups(self, request, model_admin):
        return (
            ('name', 'Category Name'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'name':
            return queryset.order_by('name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_filter = [CategoryNameFilter]

    search_fields = ['name']


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    fields = ['post', 'author', 'comment', 'parent']
    list_display = ['post', 'author', 'date_create', 'last_updated', 'parent']

    search_fields = ['author__username']


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    fields = ['post', 'author']
    list_display = ['post', 'author', 'created']

    search_fields = ['author__username']
