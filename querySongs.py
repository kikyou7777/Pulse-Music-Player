def query(sp, min_BPM, max_BPM):
    
    songs = sp.recommendations(seed_genres = ['pop'], limit = 10, min_tempo = min_BPM, max_tempo = max_BPM, target_danceability = 0.6, min_energy = 0.6)
    

    for song in songs['tracks']:
        print(song['name'])

    return songs