from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from .models import Post, Category


@receiver(post_save, sender=Post)
def create_slug_for_post(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()


@receiver(post_save, sender=Category)
def create_slug_for_category(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.name)
        instance.save()
