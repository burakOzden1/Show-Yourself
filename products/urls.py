from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_view),
    path('list', views.urunler_view),
    path('<urun_adi>', views.details),
    path('kategori/<int:category_id>', views.getProductsByCategoryId),
    path('kategori/<str:category_name>', views.getProductsByCategory, name='products_by_category'),
]
