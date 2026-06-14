import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neurotechc.settings')
django.setup()

from core.models import Job
from core.db import save_job_to_mongodb

def run_migration():
    jobs = Job.objects.all()
    count = 0
    for job in jobs:
        data = {
            'job_title': job.job_title,
            'description': job.description,
            'experience_level': job.experience_level,
            'employment_type': job.employment_type,
            'location': job.location,
            'salary_min': job.salary_min,
            'salary_max': job.salary_max,
            'skills_required': job.skills_required,
            'apply_link': job.apply_link,
            'is_active': job.is_active,
        }
        save_job_to_mongodb(data)
        count += 1
    print(f"Successfully migrated {count} jobs to MongoDB!")

if __name__ == '__main__':
    run_migration()
