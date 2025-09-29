from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Post
from . serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# By Ezekiel Minja
# M Enterprise

@api_view(['GET'])
def post_list(request):
    '''Gets all posts from the Post model in database'''
    blog_list = Post.objects.all()
    serializer = PostSerializer(blog_list, many=True)
    return Response (serializer.data)

@api_view(['GET'])
def user_list(request):
    '''Gets all users from the user model in database'''
    users = User.objects.all()
    serializer = UserSerializer(users, many = True,context = {'request':request})
    return Response(serializer.data)

@api_view(['GET'])
def user_detail(request,pk):
    '''Gets user by id'''
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user, context = {'request':request})
    return Response(serializer.data)