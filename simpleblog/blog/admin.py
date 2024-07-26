from django.apps import AppConfig
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


class BlogConfig(AppConfig):
    name = 'blog'


admin.site.register(Post, PostAdmin)
