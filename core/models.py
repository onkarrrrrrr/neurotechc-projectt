from django.db import models

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('DV', 'Design Verification'),
        ('RTL', 'RTL Design'),
        ('FPGA', 'FPGA Prototyping'),
        ('UVM', 'UVM Testbench'),
        ('COVERAGE', 'Functional Coverage'),
        ('EMBEDDED', 'Embedded Systems'),
        ('CONSULTING', 'General Consulting'),
    ]
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('CONTACTED', 'Contacted'),
        ('COMPLETED', 'Completed'),
        ('CANCELED', 'Canceled'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=200, blank=True)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='NEW')
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.get_service_display()}"


class Job(models.Model):
    EXPERIENCE_LEVEL_CHOICES = [
        ('ENTRY', 'Entry Level'),
        ('MID', 'Mid Level'),
        ('SENIOR', 'Senior Level'),
        ('LEAD', 'Lead'),
        ('MANAGER', 'Manager'),
    ]
    
    EMPLOYMENT_TYPE_CHOICES = [
        ('FULL_TIME', 'Full Time'),
        ('CONTRACT', 'Contract'),
        ('PART_TIME', 'Part Time'),
        ('INTERNSHIP', 'Internship'),
    ]
    
    job_title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default='FULL_TIME')
    location = models.CharField(max_length=200, blank=True, null=True)
    salary_min = models.IntegerField(null=True, blank=True)
    salary_max = models.IntegerField(null=True, blank=True)
    skills_required = models.TextField(help_text="Enter skills separated by commas", blank=True, null=True)
    apply_link = models.URLField(default='https://www.linkedin.com/company/neurotech-circuits-private-limited/jobs/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.job_title} - {self.get_experience_level_display()}"
