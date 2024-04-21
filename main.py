
# Spotify credentials below (someone please remind me to cancel this premium account after we present)
# username: eitproject
# passcode: 123eitproject
import serial_connection
import spotify_authorization
import querySongs

#Uncomment the two codes below to test with the arduino/get rid of hardcode

# min_BPM, max_BPM = serial_connection.read()
sp = spotify_authorization.authorization()
# songs = querySongs.query(sp, min_BPM, max_BPM)
songs = querySongs.query(sp, 100, 120)
