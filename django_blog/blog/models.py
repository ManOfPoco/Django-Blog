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


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"Comment by {self.author.username} for {self.post.title}"


class PostCommentReply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        PostComment, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now_add=True)
    reply_comment = models.TextField()
    parent_reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"Comment by {self.author.username} for {self.comment.comment}"

    def get_all_replies(self):
        all_replies = list(self.replies.all())
        for reply in all_replies:
            all_replies.extend(reply.get_all_replies())
        return all_replies
