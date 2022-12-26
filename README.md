__1.programs need to install __
  python 
  pycharm
  sqlit3

#2.libraryies in python #
  django
  djangorestframework

#3.in pycharm tirminal  create a Django app, first create a project called DjangoAPI#

  '''django-admin startproject DjangoAPI'''

#4.create a Django app called TaskPart1:
  '''django-admin startapp Task1Part1'''
 
#5.Register the App Project Settings in DjangoAPI->settings.py#
   '''
 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'Task1Part1.apps.Task1Part1Config'
]


CORS_ORIGIN_ALLOW_ALL =True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    '''
    
    
#6.Register App URLs in DjangoAPI->urls.py#
  '''
    from django.conf.urls import url,include
    from django.contrib import admin
    from django.urls import path



    urlpatterns = [
        path('admin/', admin.site.urls),
        url(r'^',include('Task1Part1.urls'))
    ]
  '''
  
  
  
  #7.in Task1Part1->apps.py make app add#
  
        '''
           from django.apps import AppConfig
           class Task1Part1Config(AppConfig):
                default_auto_field = 'django.db.models.BigAutoField'
                name = 'Task1Part1'

        '''
    
   #8.Create a Model for the App Task1Part1->create pthon file named model.py#
      '''
          from django.db import models
          class Post(models.Model):
              id = models.AutoField(primary_key=True)
              title = models.CharField(max_length=500)
              text = models.TextField()
          '''
      
    #9.Make Migrations#
      ''' python manage.py makemigrations Task1Part1'''
      '''python manage.py migrate'''
      
    #10. Serialize the Model in Task1Part1-> create python file named serializer.py#
          '''
              from rest_framework import serializers
              from .model import Post
              class PostSerializer(serializers.ModelSerializer):
                  class Meta:
                      model = Post
                      fields = ('id', 'title', 'text')

          '''
          
   #11.make view and add for database create file in Task1Part1->views.py#
            ''' from django.http import JsonResponse
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
               '''
  #12.Create a URL Path for the App in Task1Part1 create python file named urls.py#
            '''

              from django.conf.urls import url
              from .views import PostApi
              from django.conf.urls.static import static
              from django.conf import settings

              urlpatterns = [
                  url(r'^Post$', PostApi),

              ]

            '''
#13. run server #
      '''python manage.py runserver'''

#14. need postman to test#


#15.in Tadk1Part1->admin
      '''
          from django.contrib import admin
          from .models import Post
          admin.site.register(Post)
      '''
      
#16. in pycharm tirminal 
      '''
          python manage.py createsuperuser
      '''
      then make username and password for admin and go to the http://127.0.0.1:8000/admin/

