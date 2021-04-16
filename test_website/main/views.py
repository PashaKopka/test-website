from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views.generic.base import View
from .forms import SignUpForm


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
