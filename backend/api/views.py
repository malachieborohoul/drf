from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance: 
        data = ProductSerializer(instance).data
    return Response(data)