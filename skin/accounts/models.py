from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('PATIENT', 'Patient'),
        ('DOCTOR', 'Doctor'),
    )
    
    username = None  # Remove username field
    email = models.EmailField(_('email address'), unique=True)  # Make email the USERNAME_FIELD
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='PATIENT')
    
    # Doctor specific fields
    id_number = models.CharField(max_length=50, blank=True, help_text='National ID or License number')
    
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default
    
    def __str__(self):
        return f"{self.email} ({self.user_type})"

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
