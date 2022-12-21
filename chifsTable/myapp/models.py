from django.db import models
from unicodedata import name

# Create your models here.


class Catigoty(models.Model):
    menu_catigorys = models.CharField(max_length=200)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    count = models.IntegerField()
    catigory_id = models.ForeignKey(
        Catigoty, on_delete=models.PROTECT, default=None)


class LogForm(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField()
