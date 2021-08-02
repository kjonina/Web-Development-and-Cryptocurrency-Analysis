from django.db import models

from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(null = True)
    body = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='images/', null = True)
    slug =  models.SlugField(max_length=100,unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    # def __str__(self):
    #     return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')
