from django.db import models


class Post(models.Model):
    # objects = None
    title = models.CharField(max_length=100)
    details = models.TextField()
    author = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

