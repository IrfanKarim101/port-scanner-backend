from django.contrib import admin
from .models import CustomUser  # Assuming you have a CustomUser model for authentication

admin.site.register(CustomUser)  # Register the CustomUser model with the admin site