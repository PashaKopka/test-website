from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up')
]