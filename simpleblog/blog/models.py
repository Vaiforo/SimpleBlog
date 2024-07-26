from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', null=False)
    content = models.TextField(verbose_name='Content', null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def get_absolute_url(self):
        return reverse('post', args=[self.pk])

    def get_edit_absolute_url(self):
        return reverse('edit-post', args=[self.pk])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']
