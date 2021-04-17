from django.db import models
from django.contrib.auth import models as m
from django.utils.timezone import now


class Post(models.Model):
    """
    This is post model
    """
    name = models.CharField(max_length=150, blank=False)
    article = models.TextField(blank=False)
    image = models.ImageField(upload_to='uploads/', blank=True)
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

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            last_login=now(),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
