import webbrowser
from Body.speak import speak
from Body.listen import hearing

def tv():
    speak("whick chanel to you want to watch")
    chanel = hearing()