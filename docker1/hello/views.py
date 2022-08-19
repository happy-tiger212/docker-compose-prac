from django.views import View
from django.http  import JsonResponse
import json

from .models import User

class GreetingView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.create(
                name = data['name']
            )
            result = f"Hello, {user.name}"
            return JsonResponse({"result": result}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"message": "USER_DOES_NOT_EXIST"}, status=401)