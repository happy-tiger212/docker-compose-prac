from ipaddress import ip_address
from django.views import View
from django.http  import JsonResponse
import json

from .models import User

class GreetingView(View):
    def post(self, request):
        # try:
            data            = json.loads(request.body)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

            name = data['name']

            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')

            if not User.objects.filter(name=name, ip_address=ip).exists():
                user = User.objects.create(name = name, ip_address = ip)
                result = {
                    'name' : user.name,
                    # 'created_at' : user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                    # 'ip': user.ip_address
                }
            else:
                users = User.objects.filter(name=name, ip_address=ip)
                [user.save() for user in users]
                result = [{
                    'name' : user.name,
                    # 'created_at' : user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                    # 'ip': user.ip_address
                }for user in users]
            return JsonResponse({"result": result}, status=200)

        # except User.DoesNotExist:
        #     return JsonResponse({'message' : 'USER_DOES_NOT_EXIST'}, status=400)
        # except:
        #     return JsonResponse({"message" : "ERROR"}, status=400)
    
    def get(self, request):
        try:
            result = [{
                'name' : user.name,
                # 'created_at' : user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
                # 'ip': user.ip_address
            }for user in User.objects.all()]

            return JsonResponse({"result": result}, status=200)
        
        except:
            return JsonResponse({"message" : "ERROR"}, status=400)