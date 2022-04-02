from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    creation_date = models.DateTimeField(default=timezone.now)
    author_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="author",
    )
    upvoted_by = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Upvotes")

    @property
    def amount_of_upvotes(self):
        return self.upvoted_by.count()


class Comment(models.Model):
    parent_post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    author_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)


class Upvotes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
