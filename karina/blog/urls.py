
from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<slug:blog_id>/', views.detail, name='detail'),
]
