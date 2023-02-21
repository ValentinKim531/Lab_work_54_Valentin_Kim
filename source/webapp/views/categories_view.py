from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Products, Categories


def categories_view(request: WSGIRequest):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context=context)

def delete_category(request, pk):
    to_do = get_object_or_404(Categories, pk=pk)
    to_do.delete()
    return redirect('categories')