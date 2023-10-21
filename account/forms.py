from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 
            'class': 'form-control my-2',
            'placeholder': 'Password',
            }),
        strip=False,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 
            'class': 'form-control my-2',
            'placeholder': 'Confirm Password',
            }),
        strip=False,
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'user_type', 'password1', 'password2']        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Last Name'}),
            'user_type': forms.Select(attrs={'class': 'form-control my-2', 'placeholder': 'User Type'}),
            'email': forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Email Address'}),
        }

    def save(self, *args, **kwargs):
        
        return super().save(*args, **kwargs)
    