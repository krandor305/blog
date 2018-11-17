from django.shortcuts import render
from . import models

def index(request):
    articles=models.Article.objects.all()
    return render(request,'main/index.html',{"articles":articles})
