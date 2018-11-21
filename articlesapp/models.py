from django.db import models
from main.models import Article

class Paragraph(models.Model):
    titre=models.CharField(max_length=100,blank=True)
    texte=models.TextField(max_length=2000)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
