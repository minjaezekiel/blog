from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('home/', views.post_list, name='post-list'),
    path('create/', views.create_post, name = 'create-post'),
    path('<int:pk>/', views.post_detail, name = 'post-detail'),
    path('users/', views.user_list, name = 'users-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
]
