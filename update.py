import time
import pyautogui as gui
from Body.speak import speak


def update():
    speak("here we go let's start the window upgradation ")
    gui.press("win")
    time.sleep(0.5)
    gui.typewrite("cmd")
    time.sleep(0.5)
    gui.press("enter")
    time.sleep(0.5)
    gui.typewrite("winget update --all")
    time.sleep(1)
    gui.press('enter')
    speak("Window upgradations started ")
    time.sleep(1)
    gui.hotkey('win', 'down')
