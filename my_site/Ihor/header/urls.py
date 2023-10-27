from django.urls import path
from . import views

urlpatterns = [
    path('header/', views.index, name='index'),
]
