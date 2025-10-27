from django.contrib import admin
from .models import Category, Resource

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'uploader', 'upload_date', 'downloads']
    list_filter = ['category', 'upload_date']
    search_fields = ['title', 'description']
    readonly_fields = ['downloads']
