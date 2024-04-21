import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyMusicPlayer:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.scope = 'user-modify-playback-state user-read-playback-state user-read-private'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=self.scope
        ))

