from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
	return render(request, 'main/index.html')
