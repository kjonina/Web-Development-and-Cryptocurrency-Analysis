# Generated by Django 3.2.4 on 2021-07-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]