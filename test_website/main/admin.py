from django.contrib import admin
from .models import User, Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    model = Like
