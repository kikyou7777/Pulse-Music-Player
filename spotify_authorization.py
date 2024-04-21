import spotipy

from spotipy.oauth2 import SpotifyOAuth

client_id = "543e98d50d59492fa7cf308ef34b0257"
client_secret = "3ef131df79ae4d019798200cd79c1ea4"
redirect_uri = 'http://localhost:8888/callback'
scope = "user-read-private user-modify-playback-state"


def authorization():
    #https://spotipy.readthedocs.io/en/2.6.1/
    auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri= redirect_uri, scope = scope)
    sp = spotipy.Spotify(auth_manager=auth_manager)


    return sp