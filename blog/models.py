from django.db import models


class Blog_Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/blog/images/')
    url = models.URLField(blank=True)  # blank для открывания в новой вкладке

    objects = models.Manager()
