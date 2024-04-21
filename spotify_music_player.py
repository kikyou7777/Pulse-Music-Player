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
        self.last_bpm = None  # Store the last BPM that triggered a song change
        self.threshold = 10   # BPM change threshold to trigger a new song


    def play_song(self, bpm):
        if self.last_bpm is None or abs(self.last_bpm - bpm) >= self.threshold:
            # Only play a new song if the BPM change exceeds the threshold or if no song has been played yet
            self.last_bpm = bpm  # Update the last BPM
            tracks = self.sp.recommendations(seed_genres=['workout'], limit=1, target_tempo=bpm)['tracks']
            if tracks:
                track_uri = tracks[0]['uri']
                self.sp.start_playback(uris=[track_uri])
                print(f"Playing: {tracks[0]['name']} by {tracks[0]['artists'][0]['name']} at {bpm} BPM")

    def get_current_device(self):
        """ Returns the first available device to control playback. """
        devices = self.sp.devices()
        for device in devices['devices']:
            if device['is_active']:
                return device['id']
        return None
