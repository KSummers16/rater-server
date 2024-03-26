from django.db import models
from django.contrib.auth.models import User
from .Game import Game


class Picture(models.Model):
    picture = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pictures_added"
    )
