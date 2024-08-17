from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_list, name='faq_list'),
    path('create/', views.faq_create, name='faq_create'),
    path('<int:pk>/', views.faq_detail, name='faq_detail'),
    path('<int:pk>/update/', views.faq_update, name='faq_update'),
    path('<int:pk>/delete/', views.faq_delete, name='faq_delete'),
]
