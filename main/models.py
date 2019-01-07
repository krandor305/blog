from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titre=models.CharField(max_length=100)
    desc=models.TextField(max_length=300)
    utilisateur=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.titre