from django.urls import path
from . import views

urlpatterns = [
    # Start business urls
    path('<slug:slug>/', views.job_application, name='jobapplication'),


]
