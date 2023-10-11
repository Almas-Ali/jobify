from django import forms

from employeer.models import Employeer

class EmployeerForm(forms.ModelForm):
    class Meta:
        model = Employeer
        fields = ['name', 'email', 'phone', 'company', 'address', 'website']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'company': 'Company',
            'address': 'Address',
            'website': 'Website',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
        }

