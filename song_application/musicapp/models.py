
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length = 200, null = True)
    last_name = models.CharField(max_length = 200)
    age = models.IntegerField(max_length= 200)
    
    
class Song(models.Model):
    title = models.CharField(max_length = 200, null = True)
    date = models.DateTimeField(auto_now_add = True)
    likes = models.CharField(max_length = 200)
    artiste_id = models.CharField(max_length = 200)
    
    
class Lyric(models.Model):
    content = models.CharField(max_length =500)
    song_id = models.IntegerField(max_length = 50)


def __str__(self):
    return self.age
