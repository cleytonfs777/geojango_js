from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    
def mapa(request):
    return render(request, 'mapa.html')

