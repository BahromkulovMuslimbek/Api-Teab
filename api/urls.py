from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('banner/list/', views.banner_list, name='banner_list'),
    path('product/list/', views.product_list, name='product_list'),
    path('faq/list/', views.faq_list, name='faq_list'),
    path('testimonial/list/', views.testimonial_list, name='testimonial_list'),

    path('banner/detail/<int:pk>/', views.banner_detail, name='banner_detail'),
    path('product/detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('faq/detail/<int:pk>/', views.faq_detail, name='faq_detail'),
    path('testimonial/detail/<int:pk>/', views.testimonial_detail, name='testimonial_detail'),

    path('banner/create/', views.banner_create, name='banner_create'),
    path('product/create/', views.product_create, name='product_create'),
    path('faq/create/', views.faq_create, name='faq_create'),
    path('testimonial/create/', views.testimonial_create, name='testimonial_create'),

    path('banner/update/<int:pk>/', views.banner_update, name='banner_update'),
    path('product/update/<int:pk>/', views.product_update, name='product_update'),
    path('faq/update/<int:pk>/', views.faq_update, name='faq_update'),
    path('testimonial/update/<int:pk>/', views.testimonial_update, name='testimonial_update'),
    
]