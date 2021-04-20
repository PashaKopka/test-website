from rest_framework import serializers

from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'name', 'article', 'image', 'likes_count', 'url')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('url', )
