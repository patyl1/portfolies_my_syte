from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def index(request):
    statistics = models.Statistic.objects.all()
    return render(request, 'ihor.html', {'statistics': statistics})


def single_ihor_statistic(request, statistic_id):
    statistic = models.Statistic.objects.get(pk=statistic_id)
    return render(request, 'statistics.html', {'statistic': statistic})

def ihor_highlites(request):
    return render(request, 'ihor_highlites.html' )
