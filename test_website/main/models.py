from django.db import models
from django.contrib.auth import models as m
from django.utils.timezone import now
from django.urls import reverse


class Post(models.Model):
    """
    This is post model
    """
    name = models.CharField(max_length=150, blank=False)
    article = models.TextField(blank=False)
    image = models.ImageField(upload_to='uploads/', blank=True)
    url = models.CharField(max_length=150, blank=False)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.url})

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


class Like(models.Model):
    """
    This is like model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=now())

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
