from django.urls import path
from . import views

urlpatterns = [
    path('', views.urunler),
    path('list', views.urunler),
    path('<urun_adi>', views.details),
    path('kategori/<int:category_id>', views.getProductsByCategoryId),
    path('kategori/<str:category_name>', views.getProductsByCategory),
]
