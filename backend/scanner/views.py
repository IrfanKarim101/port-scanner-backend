from django.contrib.auth.models import User
from .models import UserData
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import subprocess

@csrf_exempt
def scan(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            target = data.get('target')
            options = data.get('options', '-sV')

            if not target:
                return JsonResponse({'error': 'No target provided'}, status=400)

            result = subprocess.run(['nmap'] + options.split() + [target],
                                    capture_output=True, text=True)
            return JsonResponse({'result': result.stdout})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def save_user_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            user_data = data.get('data')

            if not username or not user_data:
                return JsonResponse({'error': 'Missing username or data'}, status=400)

            user, _ = User.objects.get_or_create(username=username)
            entry = UserData.objects.create(user=user, data=user_data)
            return JsonResponse({'id': entry.id, 'created_at': entry.created_at})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
