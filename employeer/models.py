from django.db import models
from django.urls import reverse

class Employeer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('view_employeer', args=[self.pk])

    