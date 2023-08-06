from django.shortcuts import render
from .models import Blog_Project


def all_blogs(request):
    projects = Blog_Project.objects.order_by()[:2] #упорядочить и отобразить только 2
    return render(request, 'blog/all_blogs.html', {'projects': projects})

