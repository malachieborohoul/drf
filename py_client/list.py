import requests
from getpass import getpass
auth_endpoint="http://localhost:8000/api/auth/"
password=getpass()

auth_response = requests.post(auth_endpoint, json={"username":"bsm","password":password})

print(auth_response.json()) 

if auth_response.status_code==200:
    token = auth_response.json()['token']
    headers ={
        "Authorization": f"Bearer {token}"
    }
    endpoint="http://localhost:8000/api/products/"
   
    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json()) 

 

 # ProPro
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes =[
#         authentication.SessionAuthentication,
#         TokenAuthentication
#                              ]
#     permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

#     def perform_create(self, serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')

#         if content is None:
#             content = title
#         serializer.save(content=content)

# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset= Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductUpdateAPIView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     authentication_classes=[authentication.SessionAuthentication]
#     permission_classes=[permissions.DjangoModelPermissions]
#     lookup_field = 'pk'


#     def perform_update(self, serializer):
#         instance = serializer.save()

#         if instance.content is None:
#             instance.content = instance.title


# class ProductDestroyAPIView(generics.DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class= ProductSerializer

#     def perform_destroy(self, instance):
#         return super().perform_destroy(instance)



# @api_view(['GET', 'POST'])
# def product_alt_view(request, *args, **kwargs):
#     method = request.method
#     if method == "GET":
#         pk = kwargs.get('pk')

#         if pk is not None:
#             obj = get_object_or_404(Product,pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         else:
#             queryset = Product.objects.all()
#             data = ProductSerializer(queryset, many=True).data
#             return Response(data)
#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content')

#             if content is None:
#                 content = title
#             serializer.save()
#             return Response(serializer.data)

