from spotify import sp

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


class ArtistService:

    def __init__(self, )
