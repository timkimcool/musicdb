from django.db import models
from django.urls import reverse

from typing import NewType
from enum import Enum
from sqlmodel import SQLModel, Field

from .core import (
    Href,
    ExternalURL,
    Image,
    ReleaseDate,
    Restriction,
    ObjType,
    Uri,
    Genre,
    Popularity,
    DatePrecision
)


class AlbumType(Enum):
    ALBUM = "album"
    SINGLE = "single"
    COMPILATION = "compilation"


class AlbumBase(models.Model, table=True):
    """Base SQLModel class"""

    id: str = Field(primary_key=True)
    album_type: AlbumType
    external_url: ExternalURL
    href: Href
    images: list[Image]
    name: str
    release_date: ReleaseDate
    release_date_precision: DatePrecision
    restriction: Restriction
    type: ObjType
    uri: Uri
    genres: list[Genre]
    popularity: Popularity
    label: str
    artists: list[Artist]
    tracks: list[Track]
    total_tracks: int

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("album_detail", args=[str(self.id)])
