from rest_framework import serializers

from .models import Post, User


# Post API serializers

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'name', 'article', 'image', 'likes_count', 'url')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('url',)


class PostCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        post = Post.objects.create(
            name=validated_data['name'],
            article=validated_data['article'],
            image=validated_data['image'],
            url=validated_data['name'].replace(' ', '-')
        )

        return post

    class Meta:
        model = Post
        fields = ('id', 'name', 'article', 'image')


# Post API serializers

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    liked_posts = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'last_login', 'username', 'email', 'date_joined', 'last_request', 'posts', 'liked_posts')


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
