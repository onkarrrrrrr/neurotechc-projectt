from django.contrib import admin
from .models import Appointment, Job

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'company', 'service', 'status', 'created_at')
    list_filter = ('service', 'status', 'created_at')
    search_fields = ('full_name', 'email', 'company')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'employment_type', 'experience_level', 'apply_link', 'is_active', 'created_at')
    list_filter = ('experience_level', 'is_active', 'created_at')
    search_fields = ('job_title',)
    readonly_fields = ('created_at', 'updated_at')
    
    fields = ('job_title', 'employment_type', 'experience_level', 'apply_link')
