from contextlib import nullcontext
from operator import mod
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(_MAX_LENGTH = 200, null = True)
    last_name = models.CharField(_MAX_LENGTH = 200)
    age = models.IntegerField(_MAX_LENGTH =200)
    
    
class Song(models.Model):
    title = models.CharField(_MAX_LENGTH = 200, null = True)
    date = models.DateTimeField(auto_now_add = True)
    likes = models.CharField(_MAX_LENGTH = 200)
    artiste_id = models.CharField(_MAX_LENGTH = 200)
    
    
class Lyric(models.Model):
    content = models.CharField(_MAX_LENGTH =500)
    song_id = models.IntegerField(_MAX_LENGTH = 50)
