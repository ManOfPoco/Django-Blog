from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from django.utils import timezone


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

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f"{self.name}"
