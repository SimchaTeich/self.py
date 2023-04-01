def my_mp4_playlist(file_path, new_song):
    with open(file_path) as songs_file:
        songs = songs_file.readlines()

    if len(songs) < 3:
        with open(file_path, 'a') as songs_file:
            songs_file.write('\n' * (2 - len(songs)))
            songs_file.write(new_song + ';')
    
    else:
        old_song = songs[2].split(';', 1)[0]
        songs[2] = songs[2].replace(old_song, new_song)
        full_content = ''.join(songs)

        with open(file_path, 'w') as songs_file:
            songs_file.write(full_content)
    
    with open(file_path) as songs_file:
        print(songs_file.read())
