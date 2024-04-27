
# Spotify credentials below (someone please remind me to cancel this premium account after we present)
# username: eitproject
# passcode: 123eitproject
import serial
import time
import serial_connection
import spotify_authorization
import querySongs

from spotify_music_player import SpotifyMusicPlayer

#Uncomment the two codes below to test with the arduino/get rid of hardcode

# min_BPM, max_BPM = serial_connection.read()
# sp = spotify_authorization.authorization()
# songs = querySongs.query(sp, min_BPM, max_BPM)
# songs = querySongs.query(sp, 100, 120)
# def read_bpm(arduino):
#     if arduino.in_waiting > 0:
#         data = arduino.readline().decode().strip()
#         try:
#             bpm = int(data)  
#             return bpm
#         except ValueError:
#             return None
#     else:
#         print("No data available")
#         return None


def read_bpm(arduino):
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()
  
        try:
            bpm = int(data) 
            return bpm
        except ValueError:
            print("Failed to parse BPM values")
            return None
    else:
        print("No data available")
        return None


def setup_serial():
    return serial.Serial(port = 'COM4', baudrate = 115200, parity = 'N', stopbits= 1, timeout = 1)


def main():
    arduino = setup_serial()
    spotify_player = SpotifyMusicPlayer()

    start_time = 0
    duration = 0

    try:
        while True:

            if time.time()*1000 - start_time > duration:
                bpm = read_bpm(arduino)
            
                if bpm is not None:
                    print(bpm) 
                    duration = spotify_player.play_songs(bpm)
                    start_time = time.time() * 1000

                time.sleep(1)    

    except KeyboardInterrupt:
        print("Exiting application...")
    finally:
        if arduino:
            arduino.close()
    
if __name__ == '__main__':
    main()


