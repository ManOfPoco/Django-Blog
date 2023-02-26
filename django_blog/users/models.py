from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',
                              upload_to='profile_pictures')
    city = models.CharField(max_length=255, blank=True, null=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=150)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

    def __str__(self):
        return f'Profile {self.user.username} {self.user.last_name}'
