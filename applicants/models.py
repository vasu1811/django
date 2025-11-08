from django.db import models
from django.core.validators import FileExtensionValidator
from accounts.models import CustomUser


class ApplicantProfile(models.Model):
    """
    Applicant profile linked to CustomUser with role='applicant'
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='applicant_profile'
    )
    full_name = models.CharField(
        max_length=100,
        help_text="Applicant's full name"
    )
    resume = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])],
        help_text="Upload resume (PDF, DOC, DOCX only)"
    )
    skills = models.TextField(
        help_text="List your key skills (comma-separated)"
    )
    education = models.TextField(
        help_text="Educational background and qualifications"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.user.username}"
    
    class Meta:
        verbose_name = "Applicant Profile"
        verbose_name_plural = "Applicant Profiles"
