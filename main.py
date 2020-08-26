from youtube_client import YoutubeClient
from spotify_client import SpotifyClient

SPOTIFY_API_KEY = "BQADe_VpA9F_MTYuuXcW3ROAkFGObzZrLg_keYOVyqFsZJ7RNDDaDYcIKQ1tNj35zXUvlwnYgf7iKyqOuPllsLJm6joM6YHV78YUUFk9kBxZFbvaSWELG43qB3b_h2rxWzSVn_Hd9mRH2y5VcMXma86YwMg_NaaoAJzSztBsta2yj_PzDBSkg3ZJTw"

def run():
    """
    main driver code
    """
    youtube_client = YoutubeClient('./creds/client_secret.json')
    spotify_client = SpotifyClient(SPOTIFY_API_KEY)
    playlists = youtube_client.get_playlists()

    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected {chosen_playlist.title}")


    collected_songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(collected_songs)} to the spotify library")

    for song in collected_songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)

        if spotify_song_id:
            added_flag = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_flag:
                print(f"Successfully added {song.artist} - {song.track}")



if __name__ == '__main__':
    run()