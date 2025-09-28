from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Post
from . serializers import PostSerializer

# By Ezekiel Minja
# M Enterprise

@api_view(['GET'])
def post_list(request):
    blog_list = Post.objects.all()
    serializer = PostSerializer(blog_list, many=True)
    return Response (serializer.data)