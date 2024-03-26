from django.db import models
from django.contrib.auth.models import User
from .Game import Game


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
