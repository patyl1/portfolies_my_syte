from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:statistic_id>', views.single_statistic, name='single_statistic'),
    path('highlites/', views.yura_highlites, name='yura_highlites'),
]
