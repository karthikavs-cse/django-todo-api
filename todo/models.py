from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class User(AbstractUser):
    UNIT_CHOICES = [
        ('SI', 'S.I'),
        ('IMP', 'Imperial'),
    ]

    preferred_units = models.CharField(
        max_length=3,
        choices=UNIT_CHOICES,
        default='SI'
    )

# Task Model
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title