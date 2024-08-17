from django.contrib.auth.models import User
from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='banners/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    link = models.TextField(default='')


class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField()
    l_name = models.CharField(max_length=255)
    f_name = models.CharField(max_length=255)