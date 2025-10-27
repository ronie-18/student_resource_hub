from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Form for user registration"""
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    """Form for user profile updates"""
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'profile_image')

class UserProfileForm(forms.ModelForm):
    """Form for updating user profile"""
    class Meta:
        model = CustomUser
        fields = ('bio', 'profile_image')