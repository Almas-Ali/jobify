from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):

    user_type = forms.ChoiceField(
        label='Select an option',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            ('Employeer', 'Employeer'),
            ('Applicant', 'Applicant')
        ],
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'user_type', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2
