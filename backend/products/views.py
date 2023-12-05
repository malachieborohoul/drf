from rest_framework import authentication, generics, mixins, permissions

from .models import Product

from .serializers import ProductSerializer

from rest_framework.response import Response

from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .permissions import IsStaffEditorPermission

from api.authentication import TokenAuthentication

# ResponseSuccessResponseSuccessResponseSuccessRes

class ProductRetriveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
            content = title
        serializer.save(content=content)

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

        if instance.content is None:
            instance.content = instance.title



class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field='pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

@api_view(['GET', 'POST'])
def product_alt_view(request, *args, **kwargs):
    method = request.method

    if method=="GET":
        pk = kwargs.get('pk')

        if pk is not None:
            obj= get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False)
            return Response(data)
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True)
            return Response(data)
    
    if method =="POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')

            if content is None:
                content = title
            serializer.save()
            return Response(serializer.data)

    

# # ProdProdPr
# class ProductMixinView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field='pk'

#     def get(self, request, *args, **kwargs):
#         print(args, kwargs) 
#         pk=kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#      # Create
#     def perform_create(self, serializer):
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')

#         if content is None:
#             content = title
#         serializer.save(content=content)