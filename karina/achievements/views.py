from django.shortcuts import render

from .models import Achievement

# Create your views here.
def achievements(request):
    achievements = Achievement.objects
    return render(request, 'achievements/home.html', {'achievements':achievements})
