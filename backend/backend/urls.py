from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('scanner.urls')),  # ✅ no direct import of 'scan' here
]
