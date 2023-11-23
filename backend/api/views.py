from django.http import JsonResponse

def api_home(request, *arg, **kwargs):
    body = request.body
    return JsonResponse({'message':'Hi there BSM'})