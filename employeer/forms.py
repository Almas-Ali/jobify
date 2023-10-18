from django import forms

from job.models import Company, Job, Location, Tag, Application


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'website', 'logo', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'XYZ Company'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'A short description about your company'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com'
            }),
            'logo': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Logo'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'xyz-company'
            }),
        }


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'job_type', 'vacancy', 'category', 'location',
                  'company', 'salary', 'experience', 'image', 'slug', 'tags', 'is_published', 'is_closed']

        labels = {
            'title': 'Job Title',
            'description': 'Job Description',
            'job_type': 'Job Type',
            'vacancy': 'Number of Vacancy',
            'category': 'Job Category',
            'location': 'Job Location',
            'company': 'Company',
            'salary': 'Salary',
            'experience': 'Experience in years',
            'image': 'Job Image',
            'slug': 'Slug',
            'tags': 'Job Tags',
            'is_published': 'Is Published',
            'is_closed': 'Is Closed',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Job Description'
            }),
            'job_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Job Type',
                'choices': [
                    ('Part Time', 'Part Time'),
                    ('Full Time', 'Full Time'),
                    ('Remote', 'Remote'),
                    ('Internship', 'Internship'),
                    ('Contract', 'Contract'),
                    ('Temporary', 'Temporary'),
                ]
            }),
            'vacancy': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of Vacancy'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Job Category'
            }),
            'location': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Job Location'
            }),
            'company': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Company'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Salary'
            }),
            'experience': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Experience in years'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Image'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'job-title'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Job Tags'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'placeholder': 'Is Published'
            }),
            'is_closed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'placeholder': 'Is Closed'
            }),
        }

        def save(self, *args, **kwargs):
            instance = super().save(commit=False)
            instance.user = self.request.user
            instance.save()
            return instance


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location Name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'location-name'
            }),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tag Name'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'tag-name'
            }),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume', 'cover_letter', 'message']
        labels = {
            'resume': 'Resume',
            'cover_letter': 'Cover Letter',
            'message': 'Message',
        }
        widgets = {
            'resume': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Resume',
                'accept': 'application/pdf'
            }),
            'cover_letter': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cover Letter',
                'accept': 'application/pdf'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message to Employer'
            }),
        }
