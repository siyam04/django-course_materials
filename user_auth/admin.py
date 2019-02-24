from django.contrib import admin

# same app
from user_auth.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'profile_image']
    list_display_links = ['user']
    list_filter = ['user']


admin.site.register(Profile, ProfileAdmin)