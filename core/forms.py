from django import forms

class AppointmentForm(forms.Form):
    SERVICE_CHOICES = [
        ('DV', 'Design Verification'),
        ('RTL', 'RTL Design'),
        ('FPGA', 'FPGA Prototyping'),
        ('UVM', 'UVM Testbench'),
        ('COVERAGE', 'Functional Coverage'),
        ('EMBEDDED', 'Embedded Systems'),
        ('CONSULTING', 'General Consulting'),
    ]
    
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    company = forms.CharField(max_length=200, required=False)
    service = forms.ChoiceField(choices=SERVICE_CHOICES, required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)

class JobForm(forms.Form):
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

    job_title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    experience_level = forms.ChoiceField(choices=EXPERIENCE_LEVEL_CHOICES, required=True)
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE_CHOICES, required=True, initial='FULL_TIME')
    location = forms.CharField(max_length=200, required=False)
    salary_min = forms.IntegerField(required=False)
    salary_max = forms.IntegerField(required=False)
    skills_required = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter skills separated by commas")
    apply_link = forms.URLField(required=False, initial='https://www.linkedin.com/company/neurotech-circuits-private-limited/jobs/')
    is_active = forms.BooleanField(required=False, initial=True)
