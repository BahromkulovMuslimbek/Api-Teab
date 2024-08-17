from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BannerSerializer, ProductSerializer, FaqSerializer, TestimonialSerializer
from main.models import Banner, Product, Faq, Testimonial


@api_view(['GET'])
def banner_list(request):
    banners = Banner.objects.all()
    serializer_data = BannerSerializer(banners, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer_data = ProductSerializer(products, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def faq_list(request):
    banners = Faq.objects.all()
    serializer_data = FaqSerializer(banners, many=True)
    return Response(serializer_data.data)


@api_view(['GET'])
def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    serializer_data = TestimonialSerializer(testimonials, many=True)
    return Response(serializer_data.data)

@api_view(['GET'])
def banner_detail(request, pk):
    try:
        banners = Banner.objects.filter(pk=pk)
        if not banners.exists():
            return Response({'error': 'Not found'}, status=404)
        serializer_data = BannerSerializer(banners, many=True)
        return Response(serializer_data.data)
    except Banner.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)


@api_view(['GET'])
def product_detail(request, pk):
    try:
        products = Product.objects.filter(pk=pk)
        if not products.exists():
            return Response({'error': 'Not found'}, status=404)
        serializer_data = ProductSerializer(products, many=True)
        return Response(serializer_data.data)
    except Banner.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)


@api_view(['GET'])
def faq_detail(request, pk):
    try:
        faqs = Faq.objects.filter(pk=pk)
        if not faqs.exists():
            return Response({'error': 'Not found'}, status=404)
        serializer_data = FaqSerializer(faqs, many=True)
        return Response(serializer_data.data)
    except Banner.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)


@api_view(['GET'])
def testimonial_detail(request, pk):
    try:
        testimonials = Testimonial.objects.filter(pk=pk)
        if not testimonials.exists():
            return Response({'error': 'Not found'}, status=404)
        serializer_data = TestimonialSerializer(testimonials, many=True)
        return Response(serializer_data.data)
    except Banner.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)
    

@api_view(['POST'])
def banner_create(request):
    serializer = BannerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def banner_update(request, pk):
    try:
        banner = Banner.objects.get(pk=pk)
    except Banner.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BannerSerializer(banner, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def faq_create(request):
    serializer = FaqSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def faq_update(request, pk):
    try:
        faq = Faq.objects.get(pk=pk)
    except Faq.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = FaqSerializer(faq, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def testimonial_create(request):
    serializer = TestimonialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def testimonial_update(request, pk):
    try:
        testimonial = Testimonial.objects.get(pk=pk)
    except Testimonial.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TestimonialSerializer(testimonial, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)