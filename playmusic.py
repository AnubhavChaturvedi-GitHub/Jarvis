import webbrowser

def play_music_on_youtube(song_name):
    # Construct the YouTube search URL
    search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"

    # Open the search results in the default web browser
    webbrowser.open(search_url)

# Example usage:
# song_name = input("Enter the song name: ")
# play_music_on_youtube(song_name)
