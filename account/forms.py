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
        fields = ['first_name', 'last_name', 'email',
                  'user_type', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Last Name'}),
            'user_type': forms.Select(attrs={'class': 'form-control my-2', 'placeholder': 'User Type'}),
            'email': forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Email Address'}),
        }

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'address', 'city', 'zip_code', 'country', 'bio', 'image', 'skills', 'gender', 'interested_in']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address': 'Address',
            'city': 'City',
            'zip_code': 'Zip Code',
            'country': 'Country',
            'bio': 'Bio',
            'image': 'Profile Image',
            'skills': 'Skills',
            'gender': 'Gender',
            'interested_in': 'Interested In',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'City'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Zip Code'}),
            'country': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Country'}),
            'bio': forms.Textarea(attrs={'class': 'form-control my-2', 'placeholder': 'Bio'}),
            'image': forms.FileInput(attrs={'class': 'form-control my-2'}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-control my-2', 'placeholder': 'Select Skills'}),
            'gender': forms.Select(attrs={'class': 'form-control my-2'}),
            'interested_in': forms.Select(attrs={'class': 'form-control my-2'}),
        }
