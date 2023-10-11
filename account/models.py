from django.db import models
from django.contrib.auth.models import AbstractUser

from account.managers import UserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    bio = models.TextField()
    
    is_employer = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    is_suspend = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def is_admin(self):
        return self.is_superuser

    def suspend(self):
        self.is_suspend = True
        self.is_active = False
        self.save()

    def unsuspend(self):
        self.is_suspend = False
        self.is_active = True
        self.save()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'