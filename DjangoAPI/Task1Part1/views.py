from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .model import Post
from .serializer import PostSerializer


@csrf_exempt
def PostApi(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)
    elif request.method == 'POST':
        posts_data = JSONParser().parse(request)
        posts_serializer = PostSerializer(data=posts_data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
