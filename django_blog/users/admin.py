from django.contrib import admin
from .models import Profile, Follow


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'city', 'about']


admin.site.register(Follow)
