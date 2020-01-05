from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('registration/', views.registration, name='registration'),
    path('recognition/', views.recognition, name='recognition'),
    path('image_saved', views.image_capture, name='recognition'),
]