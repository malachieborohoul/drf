from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instan