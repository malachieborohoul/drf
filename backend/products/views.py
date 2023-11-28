from rest_framework import generics

from .models import Product

from .serializers import ProductSerializer

from rest_framework.response import Response

from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

# 
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         # print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None

#         if content is None:
#             content =title
#         serializer.save(content=content)

# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

@api_view(['GET', 'POST'])
def product_alt_view(request, *args, **kwargs):
    method=request.method

    if method=="GET":
        pass
        # url_args
        # get request -> detail view
        # list view

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method=="POST":
        pass
        # create an item
        serialize = ProductSerializer(data=request.data)
        if serialize.is_valid(raise_exception=True):
            return Response(serialize.data)


    if method=="PUT":
        pass