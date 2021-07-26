from django.shortcuts import render

# Create your views here.
def COVID_Dashboard(request):
    return render(request, 'covid/COVID_Dashboard.html')
