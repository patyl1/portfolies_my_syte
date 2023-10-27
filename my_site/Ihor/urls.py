from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:statistic_id>/', views.single_ihor_statistic, name='single_ihor_statistic'),
    path('highlites/', views.ihor_highlites, name='ihor_highlites')
]
