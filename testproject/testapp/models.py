from django.db import models

# Create your models here.
class Text(models.Model):
    name = models.CharField()
    content = models.TextField()