from django.db.models import Exists, OuterRef, Count
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import SignUpForm, LogInForm
from .models import User, Post, Like
from .serializers import PostListSerializer, PostDetailSerializer, UserListSerializer, UserDetailSerializer, \
    UserSignUpSerializer, PostCreateSerializer, LikeCreateSerializer, AnaliticsSerializer


# HomePage

class HomePageView(View):

    def get(self, request):
        posts_list = Post.objects.all()
        likes = Post.objects.annotate(number_of_answers=Count('like'))
        return render(request, 'main/homepage.html', {'posts_list': posts_list, 'likes': likes})


# User actions views

class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'main/sign_up.html', {'sign_up_form': form})

    def post(self, request):
        form = SignUpForm(request.POST)

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if form.is_valid():
            User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user.last_login = now()
                login(request, user)
        return redirect('homepage')


class LogInView(View):

    def get(self, request):
        form = LogInForm()
        return render(request, 'main/log_in.html', {'log_in_form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user.last_login = now()
            login(request, user)
        return redirect('homepage')


# Post views

class PostDetailView(DetailView):
    model = Post
    slug_field = 'url'
    extra_context = {'likes': Post.objects.annotate(number_of_answers=Count('like'))}

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            liked_by_user=Exists(
                Like.objects.filter(
                    post_id=OuterRef('pk'),
                    user_id=self.request.user.id
                )
            )
        )
        return queryset


class LikePostView(View):

    def post(self, request, slug):
        post = Post.objects.get(id=request.POST['id'])
        user = User.objects.get(username=request.user.username)

        if request.POST['like'] == 'true':
            print('da')
            like = Like.objects.create(post=post, user=user)
        else:
            print('net')
            Like.objects.filter(post=post, user=user).delete()
        return redirect('post_detail', slug)


class CreateNewPostView(View):

    def get(self, request):
        return render(request, 'main/new_post.html', {})

    def post(self, request):
        name = request.POST['name']
        article = request.POST['article']
        image = request.FILES['image']
        url = request.POST['name'].replace(' ', '-')

        Post.objects.create(name=name, article=article, image=image, url=url)
        return redirect('homepage')


# REST API VIEWS
# Post API views

class PostListAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailAPIView(APIView):

    def get(self, request, id):
        post = Post.objects.get(id=id)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class PostCreateAPIView(CreateAPIView):
    model = Post
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostCreateSerializer


# User API views

class UserListAPIView(APIView):

    def get(self, request):
        posts = User.objects.all()
        serializer = UserListSerializer(posts, many=True)
        return Response(serializer.data)


class UserDetailAPIView(APIView):

    def get(self, request, id):
        post = User.objects.get(id=id)
        serializer = UserDetailSerializer(post)
        return Response(serializer.data)


class UserSignUpAPIView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSignUpSerializer


# Like API views

class LikePostAPIView(CreateAPIView):
    model = Like
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = LikeCreateSerializer


# Analitics API view

class AnaliticsAPIView(APIView):

    def get(self, request):
        date_from = request.GET['date_from']
        date_to = request.GET['date_to']
        likes = Like.objects.filter(date__range=[date_from, date_to])
        serializer = AnaliticsSerializer(likes, many=True)
        return Response(serializer.data)
