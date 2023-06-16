import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

from music.models.album import AlbumType

load_dotenv()

SCOPE = "user-top-read user-read-recently-played user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

artistId = str


class ArtistService:

    def __init__(self, spotifyClient: spotipy.client.Spotify):
        self._spotifyClient = spotifyClient

    def get_info(self, artistId: artistId):
        return self._spotifyClient.artist(artistId)

    def get_infos(self, artistIds: list[artistId]):
        return self._spotifyClient.artists(artistIds)

    def get_albums(self, artistId: artistId, albumType: AlbumType, limit: int = 50, offset: int = 0):
        return self._spotifyClient.artist_albums(artistId, album_type=albumType, limit=limit, offset=offset)

    def get_related_artists(self, artistId: artistId):
        return self._spotifyClient.artist_related_artists(artistId)

    def get_top_tracks(self, artistId: artistId, country: str = "US"):
        return self._spotifyClient.artist_top_tracks(artistId, country=country)


trackId = str


class TrackService:

    def __init__(self, spotifyClient: spotipy.client.Spotify):
        self._spotifyClient = spotifyClient

    def get_info(self, trackId: trackId):
        return self._spotifyClient.track(trackId)

    def get_infos(self, trackIds: list[trackId]):
        return self._spotifyClient.tracks(trackIds)

    def get_audio_analysis(self, trackId: trackId):
        return self._spotifyClient.artist_albums(trackId)

    def get_audio_features(self, trackIds: list[trackId]):
        return self._spotifyClient.audio_features(trackIds)


albumId = str


class AlbumService:

    def __init__(self, spotifyClient: spotipy.client.Spotify):
        self._spotifyClient = spotifyClient

    def get_info(self, albumId: albumId):
        return self._spotifyClient.album(albumId)

    def get_infos(self, albumIds: list[albumId]):
        return self._spotifyClient.albums(albumIds)

    def get_tracks(self, albumId: albumId, limit: int = 50, offset: int = 0):
        return self._spotifyClient.album_tracks(albumId, limit, offset)


userId = str
playlist_id = str


class UserService:

    def __init__(self, spotifyClient: spotipy.client.Spotify):
        self._spotifyClient = spotifyClient

    # Current user stuff

    def get_info(self):
        return self._spotifyClient.current_user()

    def get_followed_artists(self):
        return self._spotifyClient.current_user_followed_artists()

    def get_recently_played(self, limit: int = 50, after: None = 0, before: int = None):
        return self._spotifyClient.current_user_recently_played(limit=limit, after=after, before=before)

    def is_user_following_artists(self, artistIds: list[artistId]) -> bool:
        return self._spotifyClient.current_user_following_artists(artistIds)

    def is_user_following_user(self, userIds: list[userId]) -> bool:
        return self._spotifyClient.current_user_following_users(userIds)

    def top_artists(self, limit: int = 50, offset: int = 0, time_range: str = "medium_term"):
        return self._spotifyClient.current_user_top_artists(limit=limit, offset=offset, time_range=time_range)

    def top_tracks(self, limit: int = 50, offset: int = 0, time_range: str = "medium_term"):
        return self._spotifyClient.current_user_top_tracks(limit=limit, offset=offset, time_range=time_range)

    # Album
    def get_saved_albums(self, limit: int = 50, offset: int = 0):
        return self._spotifyClient.current_user_saved_albums(limit=limit, offset=offset)

    def add_albums(self, albumIds: list[albumId]):
        return self._spotifyClient.current_user_saved_albums_add(albumIds)

    def saved_albums_contains(self, albumIds: list[albumId]):
        return self._spotifyClient.current_user_saved_albums_contains(albumIds)

    def delete_albums(self, albumIds: list[albumId]):
        return self._spotifyClient.current_user_saved_albums_delete(albumIds)

    # Track
    def get_saved_tracks(self, limit: int = 50, offset: int = 0):
        return self._spotifyClient.current_user_saved_tracks(limit=limit, offset=offset)

    def add_tracks(self, trackIds: list[trackId]):
        return self._spotifyClient.current_user_saved_tracks_add(trackIds)

    def saved_tracks_contains(self, trackIds: list[trackId]):
        return self._spotifyClient.current_user_saved_tracks_contains(trackIds)

    def delete_tracks(self, trackIds: list[trackId]):
        return self._spotifyClient.current_user_saved_tracks_delete(trackIds)

    # playlist
    def get_playlists(self, limit: int = 50, offset: int = 0):
        return self._spotifyClient.current_user_playlists(limit=limit, offset=offset)

    def unfollow_playlist(self, playlist_id: playlist_id)
        return self._spotifyClient.current_user_unfollow_playlist(playlist_id)
    # Actions


class SearchService:
    def __init__(self, spotifyClient: spotipy.client.Spotify):
        self._spotifyClient = spotifyClient


"""

add_to_queue(uri, device_id=None)
    Adds a song to the end of a user’s queue

"""
