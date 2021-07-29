
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<slug:slug>/', views.detail, name='detail'),
]
