from django.contrib import admin
from .models import Post, Category, PostComment, PostLike


class Admin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name in ['body']:
            kwargs['strip'] = False
        return super().formfield_for_dbfield(db_field, request, **kwargs)


admin.site.register((Post, Category, PostComment, PostLike))
