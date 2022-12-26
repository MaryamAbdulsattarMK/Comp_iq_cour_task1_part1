# Comp_iq_cour_task1_part1



2.libraryies in python 
  django
  djangorestframework

3.in pycharm tirminal  create a Django app, first create a project called DjangoAPI

  '''django-admin startproject DjangoAPI'''

4.create a Django app called TaskPart1:
  '''django-admin startapp Task1Part1'''
 
5.Register the App Project Settings in DjangoAPI->settings.py
   '''
  # Application definition

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
    
    
6.Register App URLs in DjangoAPI->urls.py
  '''
    from django.conf.urls import url,include
    from django.contrib import admin
    from django.urls import path



    urlpatterns = [
        path('admin/', admin.site.urls),
        url(r'^',include('Task1Part1.urls'))
    ]
  '''
  
  
  
  7.Create a URL Path for the App in Task1Part1 create python file named urls.py
    '''
    
      from django.conf.urls import url
      from .views import PostApi
      from django.conf.urls.static import static
      from django.conf import settings

      urlpatterns = [
          url(r'^Post$', PostApi),
          

      ]

    '''
