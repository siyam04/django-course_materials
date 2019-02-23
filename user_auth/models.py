from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile Information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_img', blank=True)

    def __str__(self):
        return self.user.username


