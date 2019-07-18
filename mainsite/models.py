from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    contents = models.TextField()
    Lookup = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)