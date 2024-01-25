from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'pages/index.html')


def contact_view(request):
    return render(request, 'products/contact.html')


def about_view(request):
    return render(request, 'products/about.html')