from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# ProductDetailAPPro
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


 