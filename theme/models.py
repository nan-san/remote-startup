from django.db import models

class Sort(models.Model):
    name = models.CharField(max_length=150)
    Level = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')