from django.shortcuts import render
from .decorator import decorator


def index(request):
    return render(request, 'dashboard/index.html')

def contact(request):
    return render(request, 'dashboard/contact.html')

def email(request):
    return render(request, 'dashboard/email.html')

def login(request):
    return render(request, 'dashboard/login.html')

def media(request):
    return render(request, 'dashboard/media_gallery.html')

def profile(request):
    return render(request, 'dashboard/profile.html')

def tables(request):
    return render(request, 'dashboard/tables.html')

'''CRUD'''

def banner_delete(request):
    return render(request, 'back-office/banner/delete.html')

def banner_details(request):
    return render(request, 'back-office/banner/details.html')

def banner_form(request):
    return render(request, 'back-office/banner/form.html')

def banner_list(request):
    return render(request, 'back-office/banner/list.html')

def faq_delete(request):
    return render(request, 'back-office/faq/delete.html')

def faq_details(request):
    return render(request, 'back-office/faq/details.html')

def faq_form(request):
    return render(request, 'back-office/faq/form.html')

def faq_list(request):
    return render(request, 'back-office/faq/list.html')

def product_delete(request):
    return render(request, 'back-office/product/delete.html')

def product_details(request):
    return render(request, 'back-office/product/details.html')

def product_form(request):
    return render(request, 'back-office/product/form.html')

def product_list(request):
    return render(request, 'back-office/product/list.html')

def testimonial_delete(request):
    return render(request, 'back-office/testimonial/delete.html')

def testimonial_details(request):
    return render(request, 'back-office/testimonial/details.html')

def testimonial_form(request):
    return render(request, 'back-office/testimonial/form.html')

def testimonial_list(request):
    return render(request, 'back-office/testimonial/list.html')