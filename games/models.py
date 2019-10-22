from django.db import models
from guests.models import Guest


# Create your models here.
class GameRent(models.Model):
    userId = models.ForeignKey(Guest, models.CASCADE)
    game = models.CharField(max_length=200)
