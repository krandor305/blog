from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404

def index(request):
    articles=models.Article.objects.all()
    return render(request,'main/index.html',{"articles":articles})

