from django.shortcuts import render
from .models import Thesis


def thesis(request):
    thesis = Thesis.objects
    return render(request, 'thesis/thesis_home.html', {'thesis': thesis})
