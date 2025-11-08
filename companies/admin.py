from django.contrib import admin
from .models import CompanyProfile


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    """
    Company Profile Admin
    """
    list_display = ('company_name', 'user', 'location', 'website', 'created_at')
    list_filter = ('location', 'created_at')
    search_fields = ('company_name', 'user__username', 'location')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'company_name', 'location')
        }),
        ('Details', {
            'fields': ('website', 'description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
