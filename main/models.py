from django.db import models

class Article(models.Model):
    titre=models.CharField(max_length=100)
    desc=models.CharField(max_length=150)
