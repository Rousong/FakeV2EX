from django.urls import path
from . import views

app_name = 'workout'

urlpatterns = [
    path('', views.toolview, name='tool'),
]