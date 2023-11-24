import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from products.models import Product
def api_home(request, *arg, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data ={}
    if model_data:
        data = model_to_dict(model_data )
    return JsonResponse(data)    

