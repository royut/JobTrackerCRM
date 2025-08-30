from django.shortcuts import render
from .forms import CreateJobForm

# Create your views here.
def create_job_view(request):
    form = CreateJobForm()
    return render(request, 'Job/create_job.html', {'form': form})