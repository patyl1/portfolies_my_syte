from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def index(request):
    statistics = models.Statistic.objects.all()
    return render(request, 'yura.html', {'statistics': statistics})

def single_statistic(request, statistic_id):
    statistic = models.Statistic.objects.get(pk=statistic_id)
    return render(request, 'statistics.html', {'statistic': statistic})

def yura_highlites(request):
    return render(request, 'yura_highlites.html' )

