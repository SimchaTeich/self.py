def find_longest_song(songs):
    """
    find the name of the longest songs
    int the list of songs.
    :param songs: list of songs.
                  all song is a list of
                  three items: [name, creators, time]
    :type songs: list of lists.
    :return: song name as explain abouv
    :rtype: str
    """
    return sorted(songs, key=lambda song: song[-1], reverse=True)[0][0]


def find_creator_appear_most(songs):
    """
    find the name of the creator appears
    in the most of songs.
    :param songs: list of songs.
                  all song is a list of
                  three items: [name, creators, time]
    :type songs: list of lists.
    :return: song name as explain abouv
    :rtype: str
    """
    creators = [song[1] for song in songs]
    creators_appearance = [(creator, creators.count(creator)) for creator in creators]
    return sorted(creators_appearance, key=lambda creator: creator[-1], reverse=True)[0][0]


def my_mp3_playlist(file_path):
    with open(file_path) as songs_file:
        songs = [song_details.split(';')[:-1] for song_details in songs_file.readlines()]
    
    longest_song = find_longest_song(songs)
    num_of_songs = len(songs)
    creator_appear_most = find_creator_appear_most(songs)

    return longest_song, num_of_songs, creator_appear_most
