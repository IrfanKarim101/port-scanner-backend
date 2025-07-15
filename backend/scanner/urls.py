from django.urls import path
from .views import scan, save_user_data

urlpatterns = [
    path('scan/', scan),
    path('save/', save_user_data),  # New endpoint
]
