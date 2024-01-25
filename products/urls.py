from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list', views.index),
    path('<urun_adi>', views.details),
    path('kategori/<int:category_id>', views.getProductsByCategoryId),
    path('kategori/<str:category_name>', views.getProductsByCategory, name='products_by_category'),
]
