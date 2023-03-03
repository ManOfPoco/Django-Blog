from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils import timezone

from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now=True)
    last_updated = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', blank=True)

    def __str__(self):
        return f"Post by {self.author.username} - {self.title}"

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug, 'pk': self.id})


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    image = models.ImageField(default='category_default.png',
                              upload_to='category_pictures')

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f"{self.name}"


class PostComment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True,
                            related_name='children')

    def __str__(self):
        return f"Comment by {self.author.username} for {self.post.title}"

    class MPTTMeta:
        order_insertion_by = ['comment']


class PostLike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.post.title} liked by {self.author}'

    class Meta:
        unique_together = ('post', 'author')
