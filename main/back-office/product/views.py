from django.shortcuts import render, get_object_or_404, redirect
from main import models

def product_list(request):
    products = models.Product.objects.all()
    return render(request, 'back-office/product/list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    return render(request, 'back-office/product/detail.html', {'product': product})

def product_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        product = models.Product(name=name, description=description, price=price, image=image)
        product.save()
        return redirect('product_list')
    return render(request, 'back-office/product/form.html')

def product_update(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    if request.method == "POST":
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        return redirect('product_detail', pk=product.pk)
    return render(request, 'back-office/product/form.html', {'product': product})

def product_delete(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'back-office/product/delete.html', {'product': product})