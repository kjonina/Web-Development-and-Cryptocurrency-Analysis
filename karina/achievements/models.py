from django.db import models


class Achievement(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)


    def __str__(self):
        return self.title
