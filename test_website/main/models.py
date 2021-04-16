from django.db import models
from django.contrib.auth import models as m


class Post(models.Model):
    """
    This is post model
    """
    name = models.CharField(max_length=150, blank=False)
    article = models.TextField(blank=False)
    image = models.FileField(upload_to='uploads/', blank=True)
    likes_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class User(m.User):
    """
    This is user model
    """
    posts = models.ManyToManyField(Post, related_name='posts')
    liked_posts = models.ManyToManyField(Post, related_name='liked_posts')
    last_request = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
