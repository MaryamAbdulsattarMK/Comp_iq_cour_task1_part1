from django.conf.urls import url
from .views import PostApi

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^Post$', PostApi),
    url(r'^Post/([0-9]+)$', PostApi),


]
