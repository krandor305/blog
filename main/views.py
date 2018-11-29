from django.shortcuts import render
from .forms import AjoutarticleForm
from .models import Article
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def index(request):
    articles=Article.objects.all()
    return render(request,'main/index.html',{"articles":articles})

def ajoutarticle(request):
    if request.user.is_authenticated:
        form=AjoutarticleForm()
        if request.method=='POST':
            form=AjoutarticleForm(request.POST)
            if form.is_valid():
                form.instance.utilisateur=request.user
                form.save()
        return render(request,'main/ajoutarticle.html',{"form":form})
    else:
        return HttpResponseNotFound("<h1>La page n'a pas été trouvée</h1>")

def supprimerarticle(request,slug):
    if request.user.is_authenticated:
        Article.objects.delete(pk=slug,utilisateur=request.user)
    else:
        return HttpResponseNotFound("<h1>La page n'a pas été trouvée</h1>")

def modifierarticle(request,slug):
    article=Article.objects.get(pk=slug,utilisateur=request.user)
    try:
        if request.user.is_authenticated:
            form=AjoutarticleForm(instance=article)
            if request.method=='POST':
                form=AjoutarticleForm(request.POST,instance=article)
                if form.is_valid():
                    form.instance.utilisateur=request.user
                    form.save()
            return render(request,'main/ajoutarticle.html',{"form":form})
        else:
            return HttpResponseNotFound("<h1>La page n'a pas été trouvée</h1>")
    except Article.DoesNotExist:
        return HttpResponseNotFound("<h1>La page n'a pas été trouvée</h1>")

def moncompte(request):
    if request.user.is_authenticated:
        articles=Article.objects.filter(utilisateur=request.user)
        return render(request,'main/moncompte.html',{"articles":articles})
    else:
        return HttpResponseNotFound("<h1>La page n'a pas été trouvée</h1>")



        




