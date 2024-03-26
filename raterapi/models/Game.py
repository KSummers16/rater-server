from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="games_entered"
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    designer = models.CharField(max_length=255)
    released = models.DateField()
    player_number = models.IntegerField()
    play_time = models.IntegerField()
    age_recommendation = models.CharField(max_length=255)
    categories = models.ManyToManyField(
        "Category", through="GameCategory", related_name="games"
    )
