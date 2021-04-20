from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),

    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_up_user/', SignUpView.as_view(), name='sign_up_user'),

    path('log_in/', LogInView.as_view(), name='log_in'),
    path('log_in_user/', LogInView.as_view(), name='log_in_user'),

    path('post_detail/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post_detail/<slug:slug>/like', LikePostView.as_view(), name='like_post'),
    path('new_post', CreateNewPostView.as_view(), name='new_post'),
    path('create_new_post', CreateNewPostView.as_view(), name='create_new_post'),

    # REST API urls
    path('posts_list_api/', PostListAPIView.as_view(), name='posts_list_api'),
    path('post_detail_api/<int:id>/', PostDetailAPIView.as_view(), name='posts_detail_api'),

    path('users_list_api/', UserListAPIView.as_view(), name='users_list_api'),
    path('user_detail_api/<int:id>/', UserDetailAPIView.as_view(), name='users_detail_api'),
    path('api/sign_up/', UserSignUpAPIView.as_view(), name='sign_up_user_api'),
]
