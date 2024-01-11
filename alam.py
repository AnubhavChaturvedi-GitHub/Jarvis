from Body.speak import speak
import threading
from Works.clock import *
from main import main


def alam(text):
    text = text.replace("friday", "")
    text = text.replace("set alarm", "")
    text = text.replace(" ", "")
    text = text.replace("a.m.", " AM")
    text = text.replace("p.m.", " PM")
    speak(f"Well done sir, you have successfully set an alarm using friday for {text}")
    threading.Timer(5, set_alarm, args=(text,)).start()
    threading.Timer(5, main).start()