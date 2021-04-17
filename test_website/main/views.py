from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView

from .forms import SignUpForm, LogInForm
from .models import User, Post


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
        return redirect('sign_up')


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
        return redirect('log_in')


# Post views

class PostDetailView(DetailView):
    model = Post
    slug_field = 'url'
