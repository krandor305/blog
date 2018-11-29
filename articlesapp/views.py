from django.shortcuts import render
from . import models
from .forms import AjoutparagrapheForm
from main.models import Article
from django.shortcuts import get_object_or_404

def detailarticle(request,slug):
    nomarticle=get_object_or_404(Article,pk=slug)
    paragraphes=models.Paragraph.objects.filter(article=nomarticle)
    return render(request,'main/post.html',{"article":nomarticle,"paragraphes":paragraphes})

def ajoutparagraphe(request,slug):
    nomarticle=get_object_or_404(Article,pk=slug,utilisateur=request.user)
    if request.user.is_authenticated:
        form=AjoutparagrapheForm()
        if request.method=='POST':
            form=AjoutparagrapheForm(request.POST)
            if form.is_valid():
                form.instance.article=nomarticle
                form.save()
        return render(request,'articlesapp/formparagraphe.html',{"form":form})


