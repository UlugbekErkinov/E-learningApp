from django.db import models

from django.db.models import Avg, Count, Sum

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=64, default = 0, blank = True)
    content = models.TextField(max_length=64, default=0, blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_count')
    rate = models.PositiveIntegerField()
    content = models.TextField(max_length=64, default=0, blank=True)



