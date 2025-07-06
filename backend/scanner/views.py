import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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
