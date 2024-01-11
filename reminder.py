import datetime
import os
from Body.speak import *
from Body.listen import *


def save_pending_work(work):
    with open(r'C:\Users\vlogp\Desktop\J.A.R.V.I.S\Database\pending_works.txt', 'a') as file:
        file.write(f'{work}\n')

def get_pending_works():
    pending_works = []
    if os.path.exists(r'C:\Users\vlogp\Desktop\J.A.R.V.I.S\Database\pending_works.txt'):
        with open(r'C:\Users\vlogp\Desktop\J.A.R.V.I.S\Database\pending_works.txt', 'r') as file:
            pending_works = file.readlines()
    return pending_works

def remove_pending_work(index):
    pending_works = get_pending_works()
    if 0 <= index < len(pending_works):
        del pending_works[index]
        with open(r'C:\Users\vlogp\Desktop\J.A.R.V.I.S\Database\pending_works.txt', 'w') as file:
            file.writelines(pending_works)

def remind_pending_works():
    pending_works = get_pending_works()
    if pending_works:
        speak("Today's pending works:")
        for i, work in enumerate(pending_works):
            speak(f'{i + 1}. {work.strip()}')
    else:
        speak("No pending works today!")



# Example usage
# Assuming you have the necessary functions 'speak' and 'hearing'

def logic():
    speak("What is the work?")
    text = hearing().lower()
    speak("OK, sir! Done")
    save_pending_work(text)

    while True:
        speak("Any other work, sir?")
        text = hearing().lower()

        if "no" in text or "no thanks" in text or "nhi" in text:
            speak("OK")
            break
        else:
            save_pending_work(text)
            speak("OK, sir! Done")

# Assuming you have the 'save_pending_work' function implemented
