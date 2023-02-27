from django import template
from users.models import Profile

register = template.Library()


@register.simple_tag
def check_followers(user, follower):
    profile = Profile.objects.get(user=follower)

    return profile.followers_list.filter(
        follower=user).exists()


@register.simple_tag
def check_following(user, following):
    profile = Profile.objects.get(user=following)

    return profile.followers_list.filter(
        follower=user).exists()
