from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    EMPLOYER = 'employer'
    JOB_SEEKER = 'job_seeker'
    ROLE_CHOICES = [
        (EMPLOYER, 'Employer'),
        (JOB_SEEKER, 'Job Seeker'),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=JOB_SEEKER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv_file = models.FileField(upload_to='cvs/', blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username