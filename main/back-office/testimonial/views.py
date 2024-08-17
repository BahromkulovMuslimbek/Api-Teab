from django.shortcuts import render, get_object_or_404, redirect
from main.models import Testimonial

def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'back-office/testimonial/list.html', {'testimonials': testimonials})

def testimonial_detail(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    return render(request, 'back-office/testimonial/detail.html', {'testimonial': testimonial})

def testimonial_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')
        l_name = request.POST.get('l_name')
        f_name = request.POST.get('f_name')

        Testimonial.objects.create(
            title=title,
            description=description,
            photo=photo,
            l_name=l_name,
            f_name=f_name
        )
        return redirect('testimonial_list')
    
    return render(request, 'back-office/testimonial/form.html')

def testimonial_update(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        testimonial.title = request.POST.get('title')
        testimonial.description = request.POST.get('description')
        if 'photo' in request.FILES:
            testimonial.photo = request.FILES.get('photo')
        testimonial.l_name = request.POST.get('l_name')
        testimonial.f_name = request.POST.get('f_name')
        testimonial.save()
        return redirect('testimonial_detail', pk=testimonial.pk)
    
    return render(request, 'back-office/testimonial/form.html', {'testimonial': testimonial})

def testimonial_delete(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        testimonial.delete()
        return redirect('testimonial_list')
    return render(request, 'back-office/testimonial/delete.html', {'testimonial': testimonial})
