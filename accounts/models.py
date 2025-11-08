from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    """
    Custom User model extending Django's AbstractUser
    Adds role field to distinguish between company and applicant users
    """
    ROLE_CHOICES = [
        ('company', 'Company'),
        ('applicant', 'Applicant'),
    ]
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        help_text="Select user role"
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# Signal to create profiles when user is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically create appropriate profile when a new user is created
    """
    if created:
        if instance.role == 'company':
            from companies.models import CompanyProfile
            CompanyProfile.objects.create(
                user=instance,
                company_name=f"{instance.username}'s Company"
            )
        elif instance.role == 'applicant':
            from applicants.models import ApplicantProfile
            ApplicantProfile.objects.create(
                user=instance,
                full_name=f"{instance.first_name} {instance.last_name}".strip() or instance.username
            )
