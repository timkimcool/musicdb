import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

SCOPE = "user-top-read user-read-recently-played user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

results = sp.current_user()
print(results)
