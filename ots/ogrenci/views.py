from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def ogrenciana(request):
    return HttpResponse("Web sitesine hoşgeldiniz")

def anaen(request):
    return HttpResponse("welcome to...")