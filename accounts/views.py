import json
from django.views import View
from django.http import JsonResponse

class CacheView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message':'get cache'}, status=200)
    
    
    def post(self, request, *args, **kwargs):
        return JsonResponse({'meesage':'post cache'}, status=201)