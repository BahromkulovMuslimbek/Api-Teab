from django.shortcuts import render, get_object_or_404, redirect
from main.models import Faq

def faq_list(request):
    faqs = Faq.objects.all()
    return render(request, 'back-office/faq/list.html', {'faqs': faqs})

def faq_detail(request, pk):
    faq = get_object_or_404(Faq, pk=pk)
    return render(request, 'back-office/faq/detail.html', {'faq': faq})

def faq_create(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        Faq.objects.create(
            question=question,
            answer=answer
        )
        return redirect('faq_list')
    
    return render(request, 'back-office/faq/form.html')

def faq_update(request, pk):
    faq = get_object_or_404(Faq, pk=pk)
    if request.method == 'POST':
        faq.question = request.POST.get('question')
        faq.answer = request.POST.get('answer')
        faq.save()
        return redirect('faq_detail', pk=faq.pk)
    
    return render(request, 'back-office/faq/form.html', {'faq': faq})

def faq_delete(request, pk):
    faq = get_object_or_404(Faq, pk=pk)
    if request.method == 'POST':
        faq.delete()
        return redirect('faq_list')
    return render(request, 'back-office/faq/delete.html', {'faq': faq})
