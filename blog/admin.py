from django.contrib import admin

# App importing
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active', 'author']
    list_filter = ['author', 'title']
    list_display_links = ['title']
    list_editable = ['is_active']


admin.site.register(Post, PostAdmin)