from collections import OrderedDict

from rest_framework import serializers

from .models import Post, User, Like


# Post API serializers

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'name', 'article', 'image', 'url')


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


# User API serializers

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


# Like API serializers

class LikeCreateSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField()

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        post_id = validated_data['post_id']

        if Like.objects.filter(user_id=user_id, post_id=post_id):
            like = Like.objects.filter(user_id=user_id, post_id=post_id).delete()
        else:
            like = Like.objects.create(
                user_id=user_id,
                post_id=post_id
            )

        return like

    def to_representation(self, instance):
        try:
            data = super().to_representation(instance)
        except AttributeError:
            data = OrderedDict([('post_id', None), ('user_id', None), ('id', None)])
        return data

    class Meta:
        model = Like
        fields = ('post_id', 'user_id', 'id')


# Analitics API serializers

class AnaliticsSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer()
    user = UserDetailSerializer()

    class Meta:
        model = Like
        fields = ('id', 'post', 'user', 'date')


class AnaliticsFormatSerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

