from .models import Post
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User 


class PostModelSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields =('id', 'title','author', 'body', 'created_at', 'updated_at',)

class UserSerializer(ModelSerializer): 
    class Meta:
        model = User
        fields = ('id', 'username',)
