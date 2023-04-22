from django.db import models
from django.contrib.auth import get_user_model

from .album import AlbumBase


class Review(models.Model):
    album = models.ForeignKey(
        AlbumBase,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
