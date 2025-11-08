from django.contrib import admin
from .models import ApplicantProfile


@admin.register(ApplicantProfile)
class ApplicantProfileAdmin(admin.ModelAdmin):
    """
    Applicant Profile Admin
    """
    list_display = ('full_name', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'user__username', 'skills')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'full_name')
        }),
        ('Professional Details', {
            'fields': ('resume', 'skills', 'education')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
