from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# ProductDetailA
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


 