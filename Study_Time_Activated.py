import time
import webbrowser
from Body.speak import speak  # Assuming you have a module named 'speak' with a 'speak' function
import pyautogui as ui
import time
from Works.open_operation import open_chat_GPT
from Works.open_operation import open_googleclassroom_default

def study_time_setup():
    speak("activating Jarvis special study setup, get ready to start")
    speak("playing 7 hertz Frequency music for study")
    webbrowser.open("https://youtu.be/Pdop0MM5oTc?si=HICtjKAI7SNVGe3t")
    time.sleep(2)
    ui.hotkey("win", "m")  # Separate the keys with a comma
    time.sleep(1)
    open_chat_GPT()
    time.sleep(2)
    ui.hotkey("win", "m")  # Separate the keys with a comma
    time.sleep(1)
    open_googleclassroom_default()
    time.sleep(2)
    ui.hotkey("win", "m")  # Separate the keys with a comm
    speak("done sir , all basic requirement is done , now you can start")


import webbrowser
from Body.speak import speak  # Assuming you have a module named 'speak' with a 'speak' function
import pyautogui as ui
import time

def play_music(activity, music_url):
    speak(f"This is {activity} time. Playing music to make it special.")
    webbrowser.open(music_url)

def open_entertainment(link):
    speak("Time for entertainment! Enjoy your break.")
    webbrowser.open(link)

def wish_good_morning():
    speak("Good morning! Have a wonderful day ahead.")

def sleep_time_setup(music_url):
    speak("Getting ready for a good night's sleep.")
    play_music("sleeping", music_url)

def bath_time_setup(music_url):
    speak("Enjoy your bath time! Relax and rejuvenate.")
    play_music("bath", music_url)

def kitchen_time_setup(entertainment_link):
    speak("Let's make cooking more enjoyable!")
    open_entertainment(entertainment_link)

# Example usage
sleep_music_link = "https://youtube.com/sleepmusic"
bath_music_link = "https://youtube.com/bathmusic"
kitchen_entertainment_link = "https://youtube.com/kitchenentertainment"



