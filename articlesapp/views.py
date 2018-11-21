from django.shortcuts import render
from . import models
from main.models import Article
from django.shortcuts import get_object_or_404

def detailarticle(request,slug):
    nomarticle=get_object_or_404(Article,pk=slug)
    paragraphes=models.Paragraph.objects.filter(article=nomarticle)
    return render(request,'main/post.html',{"article":nomarticle,"paragraphes":paragraphes})
