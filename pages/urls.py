from django.urls import path
from .views import home_view, about_view, contact_view, products_detail_view

urlpatterns = [
    path('', products_detail_view),
    path('', home_view),
    path('index', home_view),
    path('contact', contact_view),
    path('about', about_view),
    
]
