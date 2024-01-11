import random
from Body.speak import speak
import pyautogui as gui
import time
import webbrowser



def shut_down():
    gui.hotkey('win', 'd')
    time.sleep(1)
    gui.hotkey('alt', 'f4')
    time.sleep(1)
    gui.press('enter')


def restart():
    gui.hotkey('win', 'd')
    time.sleep(1)
    gui.hotkey('alt', 'f4')
    time.sleep(1)
    gui.press("down")
    time.sleep(1)
    gui.press('enter')

def good_night_setup():
    speak("Good night, sir. Setting up the deep sleep music for your sleep.")
    
    choices = ['8 hour relaxing music', 'sleepy music 8 hour', 'deep sleep 8 hour',
               'medicine music 8 hour', 'raining deep sleep 8 hour']
    
    random_choice = random.choice(choices)
    
    # Construct the YouTube search URL
    search_query = f"https://www.youtube.com/results?search_query={'+'.join(random_choice.split())}"
    
    # Open the web browser with the YouTube search results
    webbrowser.open(search_query)
    speak("Sweet dreams, sir.")