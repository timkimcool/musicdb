from django.db import models
from enum import Enum

class ItemType(Enum):
    ALBUM = "album"
    ARTIST = "artist"
    TRACK = "track"


class CollectionBase(models.Model, table=True):
    """Base SQLModel class"""

    id: str = Field(primary_key=True)
    item_type: ItemType
    user: User
    review: int
    generated_review: int
    review_time:
    genres:
    spotify_id:
    review_later: bool
