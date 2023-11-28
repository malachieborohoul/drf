from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    