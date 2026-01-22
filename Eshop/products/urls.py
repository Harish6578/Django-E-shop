
from django.urls import path

from . import views

urlpatterns = [
    path('', views.productsView, name='Product'),
    path('search/',views.searchProducts,name='search_product')

]
