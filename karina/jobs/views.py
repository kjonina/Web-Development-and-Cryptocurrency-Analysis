from django.shortcuts import render

from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def COVID_Dashboard(request):
    return render(request, 'jobs/covid.html')

def AirBnB_Listing(request):
    return render(request, 'jobs/airbnb_listings.html')

def tableau_cv(request):
    return render(request, 'jobs/tableau_cv.html')
