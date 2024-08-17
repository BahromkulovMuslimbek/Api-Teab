from django.contrib import admin
from . import models


admin.site.register(models.Banner)
admin.site.register(models.Product)
admin.site.register(models.Faq)
admin.site.register(models.Testimonial)