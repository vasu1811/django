from django.db import models
from accounts.models import CustomUser


class CompanyProfile(models.Model):
    """
    Company profile linked to CustomUser with role='company'
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='company_profile'
    )
    company_name = models.CharField(
        max_length=200,
        help_text="Official company name"
    )
    website = models.URLField(
        blank=True,
        null=True,
        help_text="Company website URL"
    )
    description = models.TextField(
        blank=True,
        help_text="Company description and overview"
    )
    location = models.CharField(
        max_length=100,
        help_text="Company headquarters location"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.company_name} - {self.user.username}"
    
    class Meta:
        verbose_name = "Company Profile"
        verbose_name_plural = "Company Profiles"
