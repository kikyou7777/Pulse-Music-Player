
# Spotify credentials below (someone please remind me to cancel this premium account after we present)
# username: eitproject
# passcode: 123eitproject
import serial_connection
import spotify_authorization
import querySongs
from serial_connection import setup_serial, read_bpm
from spotify_music_player import SpotifyMusicPlayer

#Uncomment the two codes below to test with the arduino/get rid of hardcode

# min_BPM, max_BPM = serial_connection.read()
# sp = spotify_authorization.authorization()
# songs = querySongs.query(sp, min_BPM, max_BPM)
# songs = querySongs.query(sp, 100, 120)

def main():
    arduino = setup_serial(port='COM4')
    spotify_player = SpotifyMusicPlayer()

    try:
        while True:
            bpm_values = read_bpm(arduino)
            if bpm_values:
                min_BPM, max_BPM = bpm_values
                if min_BPM and max_BPM:
                    spotify_player.play_songs(min_BPM, max_BPM)
    except KeyboardInterrupt:
        print("Exiting application...")
    finally:
        if arduino:
            arduino.close()

if __name__ == '__main__':
    main()
