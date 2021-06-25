from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='images/')
