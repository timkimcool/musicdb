import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pprint

from utility import album_print, track_print, track_feature_print, artist_print, playlist_print

load_dotenv()

SCOPE = "user-top-read user-read-recently-played user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

album_id1 = "6mU3As6giMDJU8kV6Hx65B"  # DIFF
album_id2 = "3pf4ET01y2FMzmkiJnVYd1"  # REMEMBER ARCHIVE
album_id3 = "6zaisPwfcIAfdUGPj3mmGY"  # HOPE
album_id4 = "6j8x8zBChjzCn0FD7KJB7p"  # IS ANYBODY OUT THERE?
artist_id = "0IznZPMUyaPGdqfP4oqBja"
album_id = "7ko0zYM5cbztWuvDrIPb7E"
country_id = "KR"
# country_id = "US"

####################
###### ALBUMS ######
####################
# print(sp.album(album_id1).keys())

album_print("ALBUM", [sp.album(album_id)])

# track_print("ALBUM_TRACKS", sp.album_tracks(album_id1)["items"])

# album_print("ALBUMS", sp.albums([album_id1])["albums"])

# album_print("New Release KR", sp.new_releases(country_id, limit=5)["albums"]["items"])

# album_print("New Release US", sp.new_releases("US", limit=5)["albums"]["items"])

# # sp.current_user_saved_albums()
# # sp.current_user_saved_albums_add()
# # sp.current_user_saved_albums_contains()
# # sp.current_user_saved_albums_delete()

####################
###### TRACKS ######
####################
track_id1 = "3BhzgxlCzJhrkRn9rOO3mf"  # lOCO
track_id2 = "52okn5MNA47tk87PeZJLEL"  # lET YOU DOWN
track_id3 = "6niC1XoLXjDoqRew6MAtFU"  # REC
track_id4 = "1elhmWW7Bv0MOQj2gAsyoV"  # MAKE YOU SAY
tracks = [track_id1, track_id2, track_id3, track_id4]

# for item in items:
#     print(item, items[item])

# tracks = sp.current_user_top_tracks(limit=5, offset=0, time_range="medium_term")  # short, medium, long
# track_print("", tracks["items"], True)

# print(sp.track(track_id1).keys())

# track_print("TRACK", [sp.track(track_id1)])
# track_print("TRACK", [sp.track(track_id2)])
# track_print("TRACK", [sp.track(track_id3)])
# track_print("TRACK", [sp.track(track_id4)])

# track_print("TRACKS", sp.tracks(track_id4)["tracks"])

# print(sp.audio_analysis(track_id1))
# sp.audio_analysis(track_id4)

# print(sp.audio_features([track_id1])[0].keys())

# items = sp.audio_features(tracks)
# print(items)
# track_feature_print("AUDIO_FEATURES", items)

# sp.current_user_saved_tracks()
# sp.current_user_saved_tracks_add()
# sp.current_user_saved_tracks_contains()
# sp.current_user_saved_tracks_delete()
# sp.current_user_playing_track()

###################
##### ARTISTS #####
###################
artist_id1 = "0IznZPMUyaPGdqfP4oqBja"  # Coogie
artist_id2 = "6fOMl44jA4Sp5b9PpYCkzz"  # NF
artist_id3 = "13jYpBHek9LD68d1ZwWmu5"  # KHAN
artists = [artist_id1, artist_id2]

# print(sp.artist(artist_id1).keys())
# artist_print("ARTIST", [sp.artist(artist_id3)])
# artist_print("ARTISTS", sp.artists(artists)["artists"])
# album_print("ARTIST_ALBUM", sp.artist_albums(artist_id2, limit=10, offset=0)["items"], True)
# artist_print("RELATED_ARTIST", sp.artist_related_artists(artist_id1)["artists"])
# track_print("TOP_TRACK_KR_COOGIE", sp.artist_top_tracks(artist_id1)["tracks"], True)
# track_print("TOP_TRACK_US_NF", sp.artist_top_tracks(artist_id2)["tracks"], True)

# artists = sp.current_user_top_artists(limit=100, time_range="short_term")["items"]
# artist_print("top artists", artists, True)

# sp.current_user_followed_artists()
# sp.current_user_following_artists()

# items = sp.artist_albums(artist_id2, limit=50, offset=0)["items"]
# album_print("artist album", items, True)
# for item in items:
#     print(item["release_date"] + item["album_type"] + item["name"])
# print("+TEST")
# items = sp.artist_albums(artist_id1, limit=10, offset=0)["items"]
# for item in items:
#     print(item["release_date"] + item["album_type"] + item["name"])
# print("+TEST")
# items = sp.artist_albums(artist_id1, album_type="album,single,appears_on,compilation", limit=50, offset=0)["items"]
# for item in items:
#     print(item["release_date"] + item["album_group"] + str(item["total_tracks"]) + item["name"])


####################
###### SEARCH ######
####################

# query = "Coogie year:2023"
# query = "chill mix"

# newest songs of artist: filter by album release date
# query = "Coogie year:2023 genre:k-rap"
# results = sp.search(query, type="track")
# track_print("SEARCH_TRACK", results["tracks"]["items"], True)

# query = "genre:k-rap"
# results = sp.search(query, type="artist")
# album_print("SEARCH_ARTIST", results["artists"]["items"], True)
"""
You can narrow down your search using field filters.
The available filters are album, artist, track, year, upc, tag:hipster, tag:new, isrc, and genre.
Each field filter only applies to certain result types.

The artist and year filters can be used while searching albums, artists and tracks.
You can filter on a single year or a range (e.g. 1955-1960).
The album filter can be used while searching albums and tracks.
The genre filter can be used while searching artists and tracks.
The isrc and track filters can be used while searching tracks.
The upc, tag:new and tag:hipster filters can only be used while searching albums.
The tag:new filter will return albums released in the past two weeks
tag:hipster can be used to return only albums with the lowest 10% popularity.

Example value: "remaster%20track:Doxy%20artist:Miles%20Davis"

type: track, artist, album, playlist, show, episode (comma separated list)
"""
# print(results["playlists"].keys())
# playlist_print("PLAYLIST_SEARCH", results["playlists"]["items"])
# results = sp.search(query, limit=10, offset=0, type="track,album,artist")
# album_print("SEARCH_ALBUM", results["albums"]["items"], True)
# album_print("SEARCH_TRACK", results["tracks"]["items"], True)
# album_print("SEARCH_ARTIST", results["artists"]["items"], True)
# print(results.keys())


####################
#### Categories ####
####################
"""
country controls location of categories
locale controls language of categories
"""
# cat_items = sp.categories(limit=10)["categories"]
# print(cat_items["limit"], cat_items["total"])
# print("Categories US", [cat["name"] + "|" + cat["id"] for cat in cat_items["items"]])
# print("@@@@@@@@@@@@@@@@@@@@@@")
# print("@@@@@@@@@@@@@@@@@@@@@@")
# cat_items = sp.categories(limit=10, country="KR", locale="ko_KR")["categories"]
# print(cat_items["limit"], cat_items["total"])
# print("Categories Korean", [cat["name"] + "|" + cat["id"] for cat in cat_items["items"]])
# print("@@@@@@@@@@@@@@@@@@@@@@")
# print("@@@@@@@@@@@@@@@@@@@@@@")


####################
###### Genres ######
####################
# print("Genres", sp.recommendation_genre_seeds())
# print("@@@@@@@@@@@@@@@@@@@@@@")
# print("@@@@@@@@@@@@@@@@@@@@@@")
# print("@@@@@@@@@@@@@@@@@@@@@@")
# print("@@@@@@@@@@@@@@@@@@@@@@")


####################
##### Playlist #####
####################
"""
tracks or episodes

fields: comma delimitted; omitted = all returned
    use parentheses to drill down into nested object
        fields=items(track(name,href,album(name,href)))
    fields can be exclueded with exclamation
"""
# pl = sp.featured_playlists("ko_KR", "KR", timestamp=None, limit=10)
# print("PL_KEYS", pl["playlists"].keys())
# pl1 = sp.featured_playlists("ko_KR", "KR", timestamp=None, limit=10)
# playlist_print(pl1["message"], pl1["playlists"]["items"], True)
# pl2 = sp.featured_playlists("en_US", "US", timestamp=None, limit=10)
# playlist_print(pl2["message"], pl2["playlists"]["items"], True)

# category_id = "in_the_car"
# pl_id = "2BdiwjnHXRpkHH0Xy3J6cY"  # TK 2023
# results = sp.playlist(pl_id)
# print(results.keys())
# playlist_print("PLAYLIST", [results])
# pl = sp.category_playlists(category_id, country="KR", limit=50)
# print(pl["playlists"]["items"].keys())
# playlist_print("KR", pl["playlists"]["items"], True)
# pl = sp.category_playlists(category_id, country="US", limit=50)
# playlist_print("US", pl["playlists"]["items"], True)
# sp.playlist(playlist_id, fields=None)
# sp.playlist_items(playlist_id, fields=None, limit=50)
# sp.playlist_tracks(playlist_id, fields=None)


# # Manipulation
# sp.playlist_add_items()
# sp.playlist_change_details()
# sp.playlist_cover_image()
# sp.playlist_is_following()
# sp.playlist_remove_all_occurrences_of_items()
# sp.playlist_remove_specific_occurrences_of_items()
# sp.playlist_reorder_items()
# sp.playlist_replace_items()
# sp.playlist_upload_cover_image()
# sp.user_playlist_create()
# sp.user_playlist_change_details()
# sp.user_playlist_follow_playlist()
# sp.user_playlist_reorder_tracks()
# sp.user_playlist_remove_all_occurrences_of_tracks()
# sp.user_playlist_remove_specific_occurrences_of_tracks()

# sp.current_user_playlists()
# sp.current_user_follow_playlist()
# sp.current_user_unfollow_playlist()
# sp.user_playlist()
# sp.user_playlist_tracks()
