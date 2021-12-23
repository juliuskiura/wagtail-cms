from django.urls import path
from . import views

urlpatterns = [
    # Start business urls
    path('', views.contact_form_view, name='jobapplication'),


]
