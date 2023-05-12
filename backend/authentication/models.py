from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, name, email, user_type, is_officer, password=None, active=True, staff=False, admin=False, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        if not password:
            raise ValueError("Users must have password")

        user_obj = self.model(
            name = name,
            email=self.normalize_email(email),
            is_officer = is_officer,
            user_type = user_type
        )
        user_obj.set_password(password)
        user_obj.is_staff = staff
        user_obj.is_admin = admin
        user_obj.is_active = active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, name, email, password=None):
        user = self.create_user(
            name,
            email,
            password=password,
            staff=True
        )

        return user
    
    def create_superuser(self, name, email, password=None, **kwargs):
        user = self.create_user(
            name,
            email,
            is_officer = True,
            user_type = 'fabrication',
            password=password,
            staff=True,
            admin = True,
             **kwargs
        )
        user.is_superuser = True
        return user



USER_TYPE_CHOICES = (
    ('fabrication', 'Fabrication User'),
    ('sub-assembly', 'Sub-assembly User'),
    ('assembly', 'Assembly User'),
)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=25, choices=USER_TYPE_CHOICES)
    is_officer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name
    
    def __str__(self):
        return f"{self.email}-{self.user_type}"