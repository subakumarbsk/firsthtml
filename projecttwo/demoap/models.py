from django.db import models

# Create your models here.
class urdata (models.Model):
    Name=models.CharField(max_length=20, default='')
    Number=models.IntegerField(default='')
    birth=models.DateField(default='')