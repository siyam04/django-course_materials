from django.contrib.auth.models import User
from django.db import models

# user_auth app
from user_auth.models import Profile


class Post(models.Model):
    # objects = None
    title = models.CharField(max_length=100)
    details = models.TextField()
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title



