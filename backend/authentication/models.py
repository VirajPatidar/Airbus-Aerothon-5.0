from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('fabrication', 'Fabrication User'),
        ('sub-assembly', 'Sub-assembly User'),
        ('assembly', 'Assembly User'),
    )
    
    user_type = models.CharField(max_length=14, choices=USER_TYPE_CHOICES)
    is_super_user = models.BooleanField(default=False)
