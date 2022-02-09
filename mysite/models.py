from django.db import models
from django.utils import timezone

class Game(models.Model):
    name = models.CharField(max_length=40)
    gid = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now)
    bank = models.PositiveBigIntegerField(default=1000000)
    def __str__(self):
        return self.name

class GameUser(models.Model):
    name = models.CharField(max_length=20)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=0)
    money = models.PositiveBigIntegerField(default=5000)
    def __str__(self):
        return self.name


