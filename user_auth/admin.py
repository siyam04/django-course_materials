from django.contrib import admin

# same app
from user_auth.models import Profile


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'profile_name', 'email']
#     list_display_links = ['profile_name']
#     list_filter = ['user', 'profile_name']


admin.site.register(Profile)