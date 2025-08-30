from django.db import models


# Create your models here.
class Job(models.Model):
    employment_type_choices = [
        ('F', 'Full-Time'),
        ('P', 'Part-Time'),
        ('C', 'Contract'),
        ('I', 'Internship'),
    ]
    state_choices = [
        ('S', 'Saved'),
        ('A', 'Applied'),
        ('I', 'Interviewing'),
        ('O', 'Offer'),
        ('R', 'Rejected'),
        ('X', 'Archived')
    ]

    title = models.CharField(max_length=200)
    job_link = models.URLField(max_length=300)
    company = models.CharField(max_length=200)
    company_link = models.URLField(max_length=300)
    location = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=1, choices=employment_type_choices)
    compensation = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=state_choices)
    applied_date = models.DateField(auto_now_add=True)
    next_followup_date = models.DateField()
    job_description = models.TextField()
    notes = models.TextField()
