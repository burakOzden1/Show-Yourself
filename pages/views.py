from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('anasayfa')


def contact_view(request):
    return HttpResponse("İletişim")


def about_view(request):
    return HttpResponse("Hakkımızda")
