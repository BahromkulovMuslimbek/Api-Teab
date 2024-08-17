from django.urls import path
from . import views

urlpatterns = [
    path('', views.banner_list, name='banner_list'),
    path('create/', views.banner_create, name='banner_create'),
    path('<int:pk>/', views.banner_detail, name='banner_detail'),
    path('update/<int:pk>/', views.banner_update, name='banner_update'),
    path('delete/<int:pk>/', views.banner_delete, name='banner_delete'),
]
