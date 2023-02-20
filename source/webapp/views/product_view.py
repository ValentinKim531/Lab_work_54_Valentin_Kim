from django.shortcuts import render, get_object_or_404

from webapp.models import Products


# def update_view(request: WSGIRequest, pk):
#     to_do = get_object_or_404(To_do, pk=pk)
#     if request.method == "GET":
#         return render(request, 'to_do_update.html', context={'to_do': to_do})
#     to_do.title = request.POST.get('title')
#     to_do.description = request.POST.get('description')
#     to_do.text = request.POST.get('text')
#     to_do.status = request.POST.get('status')
#     to_do.execution_date = request.POST.get('execution_date')
#     to_do.save()
#     return redirect('to_do_detail', pk=to_do.pk)
#
def product_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })
#
# def delete_task(request, pk):
#     to_do = get_object_or_404(To_do, pk=pk)
#     to_do.delete()
#     return redirect('index')
