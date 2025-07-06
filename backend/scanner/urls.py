from django.urls import path
from .views import scan  # ✅ Correct: local import from the same folder

urlpatterns = [
    path('scan/', scan),
]
