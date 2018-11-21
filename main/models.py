from django.db import models

class Article(models.Model):
    titre=models.CharField(max_length=100)
    desc=models.CharField(max_length=150)

    def __str__(self):
        return self.titre