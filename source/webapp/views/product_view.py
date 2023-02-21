from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Products

def product_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })

def delete_product(request, pk):
    to_do = get_object_or_404(Products, pk=pk)
    to_do.delete()
    return redirect('products')