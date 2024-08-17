from django.shortcuts import render, get_object_or_404, redirect
from main.models import Banner

def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'back-office/banner/list.html', {'banners': banners})

def banner_detail(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    return render(request, 'back-office/banner/detail.html', {'banner': banner})

def banner_create(request):
    if request.method == 'POST':
       
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        Banner.objects.create(
            title=title,
            image=image,
            description=description
        )
        return redirect('banner_list')
    
    return render(request, 'back-office/banner/form.html')

def banner_update(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        banner.title = title
        if image:
            banner.image = image
        banner.description = description
        banner.save()
        return redirect('banner_detail', pk=banner.pk)
    
    return render(request, 'back-office/banner/form.html', {'banner': banner})

def banner_delete(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        banner.delete()
        return redirect('banner_list')
    return render(request, 'back-office/banner/delete.html', {'banner': banner})


