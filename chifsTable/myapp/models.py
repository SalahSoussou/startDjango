from django.db import models
from unicodedata import name

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField()
