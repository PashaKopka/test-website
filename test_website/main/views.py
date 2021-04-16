from django.shortcuts import render
from django.views.generic.base import View


class SignUpView(View):

    def get(self, request):
        return render(request, 'main/sign_up.html')
