from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('email/', views.email, name='email'),
    path('login/', views.login, name='login'),
    path('media/', views.media, name='media'),
    path('profile/', views.profile, name='profile'),
    path('tables/', views.tables, name='tables'),

    path('banner_delete/', views.banner_delete, name='banner_delete'),
    path('banner_details/', views.banner_details, name='banner_details'),
    path('banner_form/', views.banner_form, name='banner_form'),
    path('banner_list/', views.banner_list, name='banner_list'),

    path('faq_delete/', views.faq_delete, name='faq_delete'),
    path('faq_details/', views.faq_details, name='faq_details'),
    path('faq_form/', views.faq_form, name='faq_form'),
    path('faq_list/', views.faq_list, name='faq_list'),

    path('product_delete/', views.product_delete, name='product_delete'),
    path('product_details/', views.product_details, name='product_details'),
    path('product_form/', views.product_form, name='product_form'),
    path('product_list/', views.product_list, name='product_list'),

    path('testimonial_delete/', views.testimonial_delete, name='testimonial_delete'),
    path('testimonial_details/', views.testimonial_details, name='testimonial_details'),
    path('testimonial_form/', views.testimonial_form, name='testimonial_form'),
    path('testimonial_list/', views.testimonial_list, name='testimonial_list'),
]