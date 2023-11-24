import requests
endpoint="http://localhost:8000/api/"

get_response = requests.get(endpoint, params={'abc':123}, json={"query":"Hello world"})
# get_response = requests.get(endpoint, )

print(get_response.json()) 



# import json
# from django.forms.models import model_to_dict
# # from django.http import JsonResponse, HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from products.models import Product

# @api_view(["GET"])
# def api_home(request, *arg, **kwargs):
#     model_data = Product.objects.all().order_by('?').first()
#     data={}
#     if model_data:
#         data = model_to_dict(model_data)
#     return Response(data)  