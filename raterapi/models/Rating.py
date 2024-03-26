from django.db import models
from django.contrib.auth.models import User
from .Game import Game


class Rating(models.Model):
    score = models.IntegerField()
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
