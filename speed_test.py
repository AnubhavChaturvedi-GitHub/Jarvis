import webbrowser
from Body.speak import *

def check_internet_speed():
    speak("checking.. speed")
    webbrowser.open("https://fast.com")
    speak("speed should we there in your screen")



