import spotipy
from spotipy.oauth2 import SpotifyOAuth
#querySongs.py has been replaced with spotify_music_player.py which now handles both querying and playing songs.
class SpotifyMusicPlayer:
    def __init__(self):
        self.sp = get_spotify_client()

    def play_songs(self, min_BPM, max_BPM):
        recommendations = self.sp.recommendations(seed_genres=['workout'], limit=1,
                                                  min_tempo=min_BPM, max_tempo=max_BPM,
                                                  target_danceability=0.6, min_energy=0.6)
        if recommendations['tracks']:
            track_uri = recommendations['tracks'][0]['uri']
            self.sp.start_playback(uris=[track_uri])
            print(f"Playing: {recommendations['tracks'][0]['name']}")