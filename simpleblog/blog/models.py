from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
