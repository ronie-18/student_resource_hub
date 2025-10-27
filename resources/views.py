from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Resource, Category, Newsletter
from .forms import ResourceUploadForm, ResourceSearchForm

def home(request):
    """Home page view with featured resources"""
    featured_resources = Resource.objects.all().order_by('-downloads')[:6]
    categories = Category.objects.all()
    
    context = {
        'featured_resources': featured_resources,
        'categories': categories,
    }
    return render(request, 'resources/home.html', context)

def resource_list(request):
    """View for listing and searching resources"""
    resources = Resource.objects.all().order_by('-upload_date')
    form = ResourceSearchForm(request.GET)
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        category = form.cleaned_data.get('category')
        
        if query:
            resources = resources.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        
        if category:
            resources = resources.filter(category=category)
    
    context = {
        'resources': resources,
        'form': form,
        'categories': Category.objects.all(),
    }
    return render(request, 'resources/resource_list.html', context)

@login_required
def upload_resource(request):
    """View for uploading new resources"""
    if request.method == 'POST':
        form = ResourceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploader = request.user
            resource.save()
            messages.success(request, 'Resource uploaded successfully!')
            return redirect('resource_detail', pk=resource.pk)
    else:
        form = ResourceUploadForm()
    
    return render(request, 'resources/upload_resource.html', {'form': form})

def resource_detail(request, pk):
    """View for resource details"""
    resource = get_object_or_404(Resource, pk=pk)
    related_resources = Resource.objects.filter(category=resource.category).exclude(pk=pk)[:3]
    
    context = {
        'resource': resource,
        'related_resources': related_resources,
    }
    return render(request, 'resources/resource_detail.html', context)

@login_required
def download_resource(request, pk):
    """View for downloading resources and incrementing download count"""
    resource = get_object_or_404(Resource, pk=pk)
    resource.downloads += 1
    resource.save()
    
    # Return the file URL with context for opening in new tab
    # The template will handle opening in new tab and downloading
    context = {
        'resource': resource,
        'file_url': resource.file.url,
    }
    return render(request, 'resources/download.html', context)

def category_resources(request, pk):
    """View for resources filtered by category"""
    category = get_object_or_404(Category, pk=pk)
    resources = Resource.objects.filter(category=category).order_by('-upload_date')
    
    context = {
        'category': category,
        'resources': resources,
    }
    return render(request, 'resources/category_resources.html', context)

@require_POST
def subscribe_newsletter(request):
    """View for handling newsletter subscriptions"""
    email = request.POST.get('email')
    if email:
        # Check if email already exists
        if not Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.create(email=email)
            messages.success(request, 'Successfully subscribed to the newsletter!')
        else:
            messages.info(request, 'You are already subscribed to our newsletter.')
    else:
        messages.error(request, 'Please provide a valid email address.')
    
    # Return to the referring page or home
    return redirect(request.META.get('HTTP_REFERER', 'home'))
