from django.views.generic import ListView, DetailView

from .models.album import AlbumBase


class AlbumListView(ListView):
    model = AlbumBase
    context_object_name = "album_list"
    template_name = "music/album_list.html"


class AlbumDetailView(DetailView):
    model = AlbumBase
    context_object_name = "album"
    template_name = "music/album_detail.html"
