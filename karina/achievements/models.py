from django.db import models


class Achievement(models.Model):
    image = models.ImageField(null= True, upload_to='images/')
    pub_date = models.DateTimeField(null= True)
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)


    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')
