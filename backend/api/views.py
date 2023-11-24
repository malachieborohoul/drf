import json
from django.http import JsonResponse

def api_home(request, *arg, **kwargs):
    body = request.body
    data ={}
    try:
        data = json.loads(body)
    except:
        pass

    print(data)
    return JsonResponse(data)
