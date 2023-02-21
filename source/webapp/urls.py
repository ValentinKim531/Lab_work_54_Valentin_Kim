from django.urls import path

from webapp.views.category_add_view import category_add_view
from webapp.views.products_view import products_view
from webapp.views.product_view import product_view, delete_product

from webapp.views.product_add_view import product_add_view

urlpatterns = [
    path("", products_view, name='products'),
    path('products', products_view, name='products'),
    path('products/add', product_add_view, name='product_add'),
    path('categories/add', category_add_view, name='category_add'),
    path('products/<int:pk>', product_view, name='product_view'),
    path('product/delete/<int:pk>', delete_product, name='product_delete'),
]