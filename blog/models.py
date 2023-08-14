from django.db import models


class Blog_Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    date = models.DateField(auto_now=False)

    objects = models.Manager()

    def __str__(self):               # отображение названий в админке
        return self.title
