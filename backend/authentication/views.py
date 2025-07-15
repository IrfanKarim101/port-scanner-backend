from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate('path/to/your/firebase/credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            if not username or not password or not email:
                return JsonResponse({'error': 'All fields are required'}, status=400)

            user = User.objects.create_user(username=username, password=password, email=email)
            return JsonResponse({'message': 'User created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout successful'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)