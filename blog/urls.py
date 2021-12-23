from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('blog-json', views.get_context, name='jsonblog')
]
