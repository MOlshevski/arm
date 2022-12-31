from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
