import spotipy
import spotify_authorization
from spotipy.oauth2 import SpotifyOAuth
#querySongs.py has been replaced with spotify_music_player.py which now handles both querying and playing songs.
class SpotifyMusicPlayer:
    def __init__(self):
        self.sp = spotify_authorization.get_spotify_client()

    def play_songs(self, BPM):
  

        recommendations = self.sp.recommendations(seed_genres=['work-out'], limit=1,
                                                  target_tempo = BPM, min_energy=0.6)
       
        if recommendations['tracks']:
            track_uri = recommendations['tracks'][0]['uri']
            self.sp.start_playback(uris=[track_uri])
            print(f"Playing: {recommendations['tracks'][0]['name']}")
            return recommendations['tracks'][0]['duration_ms']