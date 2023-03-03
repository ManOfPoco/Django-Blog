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

    @property
    def followers_count(self):
        return self.user.following.count()

    @property
    def following_count(self):
        return self.user.follower.count()

    @property
    def followers_list(self):
        return self.user.following.all().order_by('-follower')

    @property
    def following_list(self):
        return self.user.follower.all().order_by('-following')

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

    def __str__(self):
        return f'Profile {self.user.username} {self.user.last_name}'


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='user_cannot_follow_himself',
                check=~models.Q(follower=models.F('following')),
                violation_error_message="User can't follow himself"
            ),
            models.UniqueConstraint(
                name='unique_follower_following',
                fields=['follower', 'following']
            )
        ]

    def __str__(self):
        return f'{self.follower} follows {self.following}'
