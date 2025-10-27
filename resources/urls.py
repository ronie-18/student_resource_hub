from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resource_list, name='resource_list'),
    path('resources/upload/', views.upload_resource, name='upload_resource'),
    path('resources/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('resources/<int:pk>/download/', views.download_resource, name='download_resource'),
    path('category/<int:pk>/', views.category_resources, name='category_resources'),
    path('newsletter/subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
]