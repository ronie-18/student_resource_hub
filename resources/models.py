from django.db import models
from django.conf import settings

class Category(models.Model):
    """Model for resource categories"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Resource(models.Model):
    """Model for educational resources"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='resources')
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resources')
    upload_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    downloads = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

class Newsletter(models.Model):
    """Newsletter subscription model"""
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email
