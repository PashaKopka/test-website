from django.db.models import Exists, OuterRef
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView

from .forms import SignUpForm, LogInForm
from .models import User, Post
from .logic import *


# HomePage

class HomePageView(View):

    def get(self, request):
        posts_list = Post.objects.all()
        return render(request, 'main/homepage.html', {'posts_list': posts_list})


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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            liked_by_user=Exists(
                User.liked_posts.through.objects.filter(
                    post_id=OuterRef('pk'),
                    user_id=self.request.user.id
                )
            )
        )
        print('queryset: ', queryset)
        return queryset


class LikePostView(View):

    def post(self, request, slug):
        post = Post.objects.get(id=request.POST['id'])
        user = User.objects.get(username=request.user.username)

        if request.POST['like'] == 'true':
            post.likes_count += 1
            user.liked_posts.add(post)
        else:
            post.likes_count -= 1
            user.liked_posts.remove(post)
        user.save()
        post.save()
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
