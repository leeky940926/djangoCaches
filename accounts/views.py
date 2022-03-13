from django.views import View
from django.http import JsonResponse
from django.core.cache import cache
from accounts.models import User

class CacheView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=1)
        
        cache.set("user_email", user.email, 3000)
        
        return JsonResponse({'message':'get cache'}, status=200)
