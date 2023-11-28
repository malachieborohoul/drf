from django.http import JsonResponse
from rest_framework.decorators import api_view

from rest_framework import serializers

from rest_framework.response import responses
from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data ={}
    if instance:
        data['title']=instance.title
        data['content']=instance.content
        data['price']=instance.price
    return JsonResponse(data)
