from django.contrib import admin
from .models import Job, JobApplication


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """
    Job Admin
    """
    list_display = ('title', 'company', 'location', 'job_type', 'is_active', 'posted_at')
    list_filter = ('job_type', 'is_active', 'posted_at', 'company__location')
    search_fields = ('title', 'company__company_name', 'location', 'description')
    readonly_fields = ('posted_at', 'updated_at')
    date_hierarchy = 'posted_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('company', 'title', 'location', 'job_type')
        }),
        ('Job Details', {
            'fields': ('description', 'salary_range', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('posted_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('company__user')


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    """
    Job Application Admin
    """
    list_display = ('applicant', 'job', 'status', 'applied_at')
    list_filter = ('status', 'applied_at', 'job__job_type')
    search_fields = ('applicant__full_name', 'job__title', 'job__company__company_name')
    readonly_fields = ('applied_at', 'updated_at')
    date_hierarchy = 'applied_at'
    
    fieldsets = (
        ('Application Information', {
            'fields': ('applicant', 'job', 'status')
        }),
        ('Cover Letter', {
            'fields': ('cover_letter',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('applied_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'applicant__user', 'job__company__user'
        )
