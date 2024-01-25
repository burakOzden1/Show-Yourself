from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'products/index.html')

def details(request):
    return HttpResponse('Merhaba')

def getProductsByCategory(request, category_name):
    return HttpResponse(f'{category_name}Dünya')

def getProductsByCategoryId(request, category_id):
    return HttpResponse(f'{category_id}asdfa')
