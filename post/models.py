from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    text=models.TextField()
    title=models.CharField(max_length=255)
    created_date=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
