from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class PostSerializer(serializers.Serializer):
    '''PostSerializer converts python dataTypes to json format or any required API format (Serializes data)
       Or 
       It converts json data or other formats back into python dataTypes
    '''
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length = 250)
    content = serializers.CharField(style = {'base_template': 'textarea.html'})
    created = serializers.DateTimeField(read_only = True)

    def create(self, validated_data):
        '''Creates an instance of the post if the data is valid'''
        return Post.objects.create(**validated_data) #unpacking the values from dict() as key,value
    
    def update(self, instance, validated_data):
        '''Updates a given post instance if the post is valid
           Forexample: The line: -> instance.title = validated_data.get('title', instance.title) 
           looks for a new title 'title' to use or keeps old value instance.title
        
        '''
        instance.title = validated_data.get('title', instance.title) 
        instance.content = validated_data.get('content', instance.content)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''User Serializer -> ModelSerializer'''
    class Meta:
        model = User
        fields = ['url','username','email']