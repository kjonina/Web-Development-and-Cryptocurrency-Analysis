
from django.db import models

class Thesis(models.Model):
    crypto = models.CharField(max_length=255)
