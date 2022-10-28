from django.db import models
from categories.models import Category
from posts.models import Post


class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(
        Category, related_name='category_tags', on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, related_name='post_tags', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name}'"
