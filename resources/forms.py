from django import forms
from .models import Resource, Category

class ResourceUploadForm(forms.ModelForm):
    """Form for uploading new resources"""
    class Meta:
        model = Resource
        fields = ['title', 'description', 'file', 'thumbnail', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ResourceSearchForm(forms.Form):
    """Form for searching resources"""
    query = forms.CharField(required=False, label='Search')
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Category'
    )