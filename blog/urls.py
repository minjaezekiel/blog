from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('create/', views.create_post, name = 'create-post'),
    path('<int:pk>/', views.post_detail, name = 'post-detail'),
    path('users/', views.user_list, name = 'users-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
]
