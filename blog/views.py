from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Post
from . serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# By Ezekiel Minja
# M Enterprise

@api_view(['POST'])
def create_post(request):
    '''Creates a new post'''
    serializer = PostSerializer(data =request.data)
    if serializer.is_valid():
        serializer.save() #calls the create method in PostSerializer
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def post_list(request):
    '''Gets all posts from the Post model in database'''
    blog_list = Post.objects.all()
    serializer = PostSerializer(blog_list, many=True)
    return Response (serializer.data)

@api_view(['GET','PUT','PATCH','DELETE'])
def post_detail(request,pk):
    '''Retrieve,update,delete post by Id
       In request.method in ['PUT','PATCH']
       If you want simplicity use:
       serializer = PostSerializer(post, data=request.data, partial=True)
       If you don’t care about differentiating PUT vs PATCH (you just want to update whatever fields are given)
 
    '''
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method in ['PUT','PATCH']:
        #put replaces all fields,patch replaces some fields 
        serializer = PostSerializer(post, data = request.data, partial = (request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        #deletes a post
        post.delete()
        return Response({'message':'Post deleted successfully'}, status = status.HTTP_204_NO_CONTENT)
        
    

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