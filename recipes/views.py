# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')

def sobre(request):
    return HttpResponse('Apresentacao sobre o projeto')

def contato(request):
    return HttpResponse('Contato para programador')
