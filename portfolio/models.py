from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='media/portfolio/images/')
    url = models.URLField(blank=True)  # blank для открывания в новой вкладке

    objects = models.Manager()

    def __str__(self):
        return self.title
