from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views.generic.base import View
from .forms import SignUpForm, LogInForm
from django.contrib.auth import authenticate, login


class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'main/sign_up.html', {'sign_up_form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.last_login = now()
            form.save()
        return redirect('sign_up')


class LogInView(View):

    def get(self, request):
        form = LogInForm()
        return render(request, 'main/log_in.html', {'log_in_form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print('da')
        return redirect('log_in')
