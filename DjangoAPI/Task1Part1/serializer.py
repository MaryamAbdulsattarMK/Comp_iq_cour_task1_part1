from rest_framework import serializers
from .models import  Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Post
        fields = ('id', 'title', 'text')
