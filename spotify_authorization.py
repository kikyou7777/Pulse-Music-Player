import spotipy
import os

from spotipy.oauth2 import SpotifyOAuth

def get_spotify_client():
    # client_id = "543e98d50d59492fa7cf308ef34b0257"
    client_id = '4d859ad2c1634d8f94f416def606356f'
    client_secret = "62ec8999dd554415add10680c9cf0aab"
    #client_secret = "3ef131df79ae4d019798200cd79c1ea4"
    cache_path = 'spotify_token_cache'

    redirect_uri = 'http://localhost:8888/callback'
    scope = "user-modify-playback-state"


    auth_manager = SpotifyOAuth(client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=redirect_uri,
                                scope=scope, cache_path = cache_path)
    return spotipy.Spotify(auth_manager=auth_manager)
