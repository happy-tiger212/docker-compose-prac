from django.views import View
from django.http  import JsonResponse
import json

from .models import User

class GreetingView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        User.objects.create(name = name)
        return JsonResponse({'message': 'Hello, ' + name}, status=201)