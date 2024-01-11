from Body.speak import speak
import spotipy
import webbrowser
from Body.listen import hearing
from Works.mouse import click_at_position
import time

username = 'music'
clientID = 'e13187ed828c42ff90b7915e9159815f'
clientSecret = '83fc70e574a74a0f9e67b7c9fe327ed3'
redirect_uri = 'http://google.com/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()


def playmusics():
    speak("which song do you want to play ? :")
    print("which song do you want to play ? :")
    text = hearing()
    search_song = text
    speak("playing" + search_song + "on spotify")
    results = spotifyObject.search(search_song, 1, 0, "track")
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)
    time.sleep(4)
    click_at_position(500, 550)

