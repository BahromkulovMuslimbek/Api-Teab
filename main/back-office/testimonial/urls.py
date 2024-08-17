from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path('create/', views.testimonial_create, name='testimonial_create'),
    path('<int:pk>/', views.testimonial_detail, name='testimonial_detail'),
    path('<int:pk>/update/', views.testimonial_update, name='testimonial_update'),
    path('<int:pk>/delete/', views.testimonial_delete, name='testimonial_delete'),
]
