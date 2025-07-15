from django.db import models

# Create your models here.

class UserData(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
