from django.forms import ModelForm
from .models import Job


class CreateJobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'