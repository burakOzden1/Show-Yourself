from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'layout.html')

    
def products_detail_view(request):
    return render(request, 'pages/product_detail.html')


def contact_view(request):
    return render(request, 'pages/contact.html')


def about_view(request):
    return render(request, 'pages/about.html')