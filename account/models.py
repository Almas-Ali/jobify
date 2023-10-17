from django.db import models
from django.contrib.auth.models import AbstractUser

from account.managers import UserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile/', blank=True)

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    bio = models.TextField()

    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        ],
        default=''
    )
    interested_in = models.CharField(
        max_length=10,
        choices=[
            ('Full Time', 'Full Time'),
            ('Part Time', 'Part Time'),
            ('Freelance', 'Freelance'),
            ('Internship', 'Internship'),
        ],
        default='Full Time'
    )
    user_type = models.CharField(
        max_length=10,
        choices=[
            ('Applicant', 'Applicant'),
            ('Employeer', 'Employeer'),
        ],
        default='Employeer'
    )

    is_employer = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    is_suspend = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def save(self, *args, **kwargs):
        self.username = self.email.split('@')[0]
        if self.user_type == 'Applicant':
            self.is_applicant = True
        elif self.user_type == 'Employeer':
            self.is_employer = True

        return super().save(*args, **kwargs)

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
