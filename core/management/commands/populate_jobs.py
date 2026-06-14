from django.core.management.base import BaseCommand
from core.models import Job


class Command(BaseCommand):
    help = 'Populate the database with sample job postings'

    def handle(self, *args, **options):
        sample_jobs = [
            {
                'job_title': 'Design Verification Engineer',
                'description': 'We are seeking an experienced Design Verification Engineer to join our semiconductor team. You will be responsible for developing comprehensive test plans, creating verification environments using industry-standard methodologies, and ensuring the quality of our RTL designs. Your expertise in SystemVerilog, UVM, and advanced coverage techniques will be crucial.',
                'experience_level': 'MID',
                'employment_type': 'FULL_TIME',
                'location': 'San Jose, CA',
                'salary_min': 130000,
                'salary_max': 170000,
                'skills_required': 'SystemVerilog, UVM, Verification, RTL Design, Coverage Analysis, SVA, FPGA',
                'apply_link': 'https://careers.example.com/apply/dv-engineer',
            },
            {
                'job_title': 'Senior RTL Design Engineer',
                'description': 'Join our design team as a Senior RTL Design Engineer. You will architect and implement complex digital designs for next-generation processors. This role requires deep expertise in Verilog/VHDL, digital design principles, and experience with modern EDA tools. Lead technical discussions and mentor junior engineers.',
                'experience_level': 'SENIOR',
                'employment_type': 'FULL_TIME',
                'location': 'Austin, TX',
                'salary_min': 160000,
                'salary_max': 210000,
                'skills_required': 'Verilog, VHDL, RTL Design, Digital Design, EDA Tools, Leadership, Timing Analysis',
                'apply_link': 'https://careers.example.com/apply/senior-rtl',
            },
            {
                'job_title': 'FPGA Prototyping Engineer',
                'description': 'We are looking for an FPGA Prototyping Engineer to design and implement hardware prototypes for our verification and prototyping platforms. You will work with Xilinx and Altera FPGA tools, develop RTL code for FPGA implementation, and validate designs on actual hardware. Experience with HLS and hardware-software co-design is a plus.',
                'experience_level': 'MID',
                'employment_type': 'FULL_TIME',
                'location': 'Mountain View, CA',
                'salary_min': 120000,
                'salary_max': 160000,
                'skills_required': 'FPGA, Xilinx Vivado, Altera Quartus, Verilog, HDL, Hardware-Software Co-Design',
                'apply_link': 'https://careers.example.com/apply/fpga-engineer',
            },
            {
                'job_title': 'UVM Testbench Developer',
                'description': 'Develop sophisticated UVM-based testbenches for complex semiconductor designs. You will create reusable verification components, develop advanced stimulus generation techniques, and implement coverage-driven verification methodologies. Deep understanding of UVM framework and object-oriented design principles required.',
                'experience_level': 'MID',
                'employment_type': 'FULL_TIME',
                'location': 'San Jose, CA',
                'salary_min': 125000,
                'salary_max': 165000,
                'skills_required': 'UVM, SystemVerilog, OOP, Testbench Development, SVA, Metrics & Analysis',
                'apply_link': 'https://careers.example.com/apply/uvm-developer',
            },
            {
                'job_title': 'Embedded Systems Engineer',
                'description': 'Build embedded software and firmware for our IoT and embedded systems solutions. You will develop drivers, implement real-time systems, and work closely with hardware teams. Proficiency in C/C++, RTOS, and embedded Linux is essential. Experience with microcontroller programming and hardware abstraction layers required.',
                'experience_level': 'MID',
                'employment_type': 'FULL_TIME',
                'location': 'Portland, OR',
                'salary_min': 110000,
                'salary_max': 150000,
                'skills_required': 'C/C++, RTOS, Embedded Linux, Microcontrollers, Device Drivers, ARM Architecture',
                'apply_link': 'https://careers.example.com/apply/embedded-engineer',
            },
            {
                'job_title': 'Junior Verification Engineer',
                'description': 'Launch your career in design verification with our mentorship program. You will work on verification projects, learn industry-standard tools and methodologies, and contribute to test development under the guidance of experienced engineers. This is an excellent opportunity for fresh graduates or career changers.',
                'experience_level': 'ENTRY',
                'employment_type': 'FULL_TIME',
                'location': 'San Jose, CA',
                'salary_min': 80000,
                'salary_max': 110000,
                'skills_required': 'Verilog, SystemVerilog, Basic Digital Design, Problem Solving, Attention to Detail',
                'apply_link': 'https://careers.example.com/apply/junior-verification',
            },
            {
                'job_title': 'Functional Coverage Analyst',
                'description': 'Specialize in functional coverage analysis and coverage-driven verification. You will develop coverage models, analyze results, and provide insights to improve verification efficiency. Expert knowledge in coverage metrics, coverage tools, and statistical analysis required.',
                'experience_level': 'SENIOR',
                'employment_type': 'FULL_TIME',
                'location': 'San Jose, CA',
                'salary_min': 140000,
                'salary_max': 180000,
                'skills_required': 'Coverage Analysis, SystemVerilog, Statistical Analysis, Metrics, Tools',
                'apply_link': 'https://careers.example.com/apply/coverage-analyst',
            },
            {
                'job_title': 'Verification Consultant (Contract)',
                'description': 'We are seeking experienced verification consultants for short-term projects. Bring your expertise in advanced verification techniques, methodology development, and training. Ideal for experienced professionals looking for flexible engagement.',
                'experience_level': 'SENIOR',
                'employment_type': 'CONTRACT',
                'location': 'Remote',
                'salary_min': 150000,
                'salary_max': 200000,
                'skills_required': 'Verification Expertise, Methodology, Training, Leadership, Advanced Techniques',
                'apply_link': 'https://careers.example.com/apply/verification-consultant',
            },
            {
                'job_title': 'Hardware Design Intern',
                'description': 'Join our design team as an intern and gain hands-on experience with RTL design and FPGA implementation. You will work on real projects, learn from experienced engineers, and contribute to our design efforts. Great opportunity for students in their final years or recent graduates.',
                'experience_level': 'ENTRY',
                'employment_type': 'INTERNSHIP',
                'location': 'San Jose, CA',
                'salary_min': 25,
                'salary_max': 35,
                'skills_required': 'Digital Design Basics, Verilog or VHDL, Learning Ability, Team Collaboration',
                'apply_link': 'https://careers.example.com/apply/design-intern',
            },
            {
                'job_title': 'Lead Verification Architect',
                'description': 'As our Lead Verification Architect, you will define verification strategies for complex projects, mentor teams, and drive innovation in verification methodologies. This is a leadership role requiring exceptional technical expertise and team management skills.',
                'experience_level': 'LEAD',
                'employment_type': 'FULL_TIME',
                'location': 'San Jose, CA',
                'salary_min': 180000,
                'salary_max': 250000,
                'skills_required': 'Verification Methodology, Team Leadership, Architecture Design, Strategic Planning',
                'apply_link': 'https://careers.example.com/apply/lead-architect',
            },
        ]

        created_count = 0
        for job_data in sample_jobs:
            job, created = Job.objects.get_or_create(
                job_title=job_data['job_title'],
                location=job_data['location'],
                defaults=job_data
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created: {job.job_title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Already exists: {job.job_title}'))

        self.stdout.write(self.style.SUCCESS(f'\n✓ Successfully created {created_count} new job postings!'))
