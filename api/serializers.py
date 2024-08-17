from rest_framework.serializers import ModelSerializer
from main.models import *


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FaqSerializer(ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class TestimonialSerializer(ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'