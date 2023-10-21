from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=1000, default='')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('core:category_detail', kwargs={'slug': self.slug})


class Company(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_companies') # One user can have multiple companies and one company can have only one user
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=5000, default='')
    website = models.URLField(max_length=100, default='')
    logo = models.ImageField(upload_to='companies')
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('core:company_detail', kwargs={'slug': self.slug})

class Tag(BaseModel):
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('core:tag_detail', kwargs={'slug': self.slug})


class Location(BaseModel):
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('core:location_detail', kwargs={'slug': self.slug})


class Skill(BaseModel):
    name = models.CharField(max_length=50, default='')
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('core:skill_detail', kwargs={'slug': self.slug})


class Job(BaseModel):
    employer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='employer_jobs') # One employer can have multiple jobs and one job can have only one employer
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_jobs') # One company can have multiple jobs and one job can have only one company
    applicants = models.ManyToManyField(get_user_model(), related_name='job_applicants', blank=True) # One applicant can apply for multiple jobs and one job can have multiple applicants
    tags = models.ManyToManyField(Tag, related_name='job_tags') # One tag can have multiple jobs and one job can have multiple tags

    title = models.CharField(max_length=100, default='') # Job Title
    short_description = models.TextField(max_length=500, default='') # Short Description
    description = models.TextField(max_length=5000, default='') # Job Description
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location_jobs') # One location can have multiple jobs and one job can have only one location
    applications = models.ManyToManyField(
        'job.Application', related_name='job_applications', 
        blank=True
        ) # One application can have multiple jobs and one job can have multiple applications
    
    views = models.IntegerField(default=0) # Number of views
    job_type = models.CharField(
        max_length=20, 
        choices=[
            ('Part Time', 'Part Time'),
            ('Full Time', 'Full Time'),
            ('Remote', 'Remote'),
            ('Internship', 'Internship'),
            ('Contract', 'Contract'),
            ('Temporary', 'Temporary'),
        ],
        default=''
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_jobs') # One category can have multiple jobs and one job can have only one category
    vacancy = models.IntegerField(default=1) # Number of vacancy
    salary = models.IntegerField(default=0) # Salary, 0 means negotiable
    experience = models.IntegerField(default=1) # Experience in years
    image = models.ImageField(upload_to='jobs') # Job Image
    slug = models.SlugField(blank=True, null=True, unique=True)
    skills = models.ManyToManyField(Skill, related_name='job_skills', blank=True) # One skill can have multiple jobs and one job can have multiple skills
    
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:job_detail', kwargs={'slug': self.slug})


class Application(BaseModel):
    job = models.ForeignKey('job.Job', on_delete=models.CASCADE, related_name='job_applications', default=None) # One job can have multiple applications and one application can have only one job
    applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='applicant_applications', default=None) # One applicant can have multiple applications and one application can have only one applicant
    resume = models.FileField(upload_to='resumes', blank=True, null=True)
    cover_letter = models.FileField(upload_to='cover_letters', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Shortlisted', 'Shortlisted'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected'),
        ],
        default='Pending'
    )
    message = models.TextField(max_length=1000, default='') # Message to employer

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return self.job.title

    # def get_absolute_url(self):
    #     return reverse('core:job_detail', kwargs={'slug': self.slug})

