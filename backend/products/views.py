from rest_framework import generics

from .models import Product

from .serializers import ProductSerializer

from rest_framework.response import Response

from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

# 
class ProductListCreateAPIView(generics.ListCreateAPIView):
    # List
    queryset = Product.objects.all()
    serializer_class= ProductSerializer

    # Create
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field='pk'

    def perform_update(self, serializer):
       instance= serializer.save()
       if instance.content is None:
           instance.content = instance.title

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)      



     