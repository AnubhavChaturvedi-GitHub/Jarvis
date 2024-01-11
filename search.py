import webbrowser
import time
import pyautogui as gui
def search_on_youtube(query):

    youtube_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(youtube_url)

def search_on_google(query):
    google_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(google_url)

def search_on_chatgpt(query):
    chatgpt_url = f"https://chat.openai.com/c/d709f894-07ea-4413-9971-fd43e19096b5"
    webbrowser.open(chatgpt_url)
    time.sleep(2)
    gui.write(f"assist me to this :{query} remember your role you are my learning assistant , try to explain every thing in shortly,call me sir from now on ")
    time.sleep(1)
    gui.press("enter")

