import requests
endpoint="http://localhost:8000/api/products/4/delete/"

# get_response = requests.get(endpoint,  json={"title":"Hello world", })
get_response = requests.delete(endpoint)

print(get_response.status_code, get_response.status_code==204) 

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


# class ProductUpdateAPIView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'

#     def perform_update(self, serializer):
#         instance = serializer.save()
#         if not instance.content:
#             instance.content = instance.title

# class ProductDeleteAPIView(generics.DestroyAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#     lookup_field='pk'
#     def perform_destroy(self, instance):
#         super().perform_destroy(instance) 
        


# @api_view(["GET", "POST"])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method=="GET":
#         if pk is not None:
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         else:
#             queryset = Product.objects.all()
#             data = ProductSerializer(queryset, many=True).data
#             return Response(data)
        
#     if method=="POST":
#         serializer=ProductSerializer(data=request.data)

#         if serializer.is_valid(raise_exception=True ):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content')

#             if content is None:
#                 content=title
#             serializer.save(content=content)
#             return Response(serializer.data)
