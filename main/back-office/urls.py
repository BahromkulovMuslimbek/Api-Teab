from django.urls import path, include

urlpatterns = [
    path('product/', include('main.back-office.product.urls')),
    path('banner/', include('main.back-office.banner.urls')),
    path('faq/', include('main.back-office.faq.urls')),
    path('testimonial/', include('main.back-office.testimonial.urls')),
    
]