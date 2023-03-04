from django.contrib import admin
from .models import Post, Category, PostComment, PostLike


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'body', 'author', 'category']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    fields = ['post', 'author', 'comment', 'parent']


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    fields = ['post', 'author']
