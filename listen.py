# 1 using chatgpt
# 2 github
# 3 explanation
# 4 line by line writing

# chat gpt code

# prompt :- give me the listen function of jarvis in python who is able to listen and recognise the text in real time to to much faster

import speech_recognition as sr
import os
import threading
from mtranslate import translate

# Function to listen for speech
def print_loop():
    while True:
        print("", end='', flush=True)

def translation_hin_to_eng(text):
    english_translation = translate(text, 'en-in')
    return english_translation
def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 35000  # Adjust this threshold based on your environment

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)


        while True:
            print("Listening....", end='', flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\rRecognizing...   ", end='', flush=True)
                recognized_text = recognizer.recognize_google(audio).lower()  # Convert to lowercase
                if recognized_text:
                    translated_text = translation_hin_to_eng(recognized_text)
                    print("\rMr.Stank: " + translated_text)
                    return translated_text  # Return the translated text
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_text = ""  # Set recognized_text to an empty string in case of error
            finally:
                print("\r", end='', flush=True)  # Erase "Listening...." and "Recognizing..."
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console after recognition


            listen_thread = threading.Thread(target=listen)
            listen_thread.start()
            print_thread = threading.Thread(target=print_loop)
            print_thread.start()

            listen_thread.join()
            print_thread.join()




def hearing():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 35000  # Adjust this threshold based on your environment

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)


        while True:
            print("Listening....", end='', flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\rRecognizing...   ", end='', flush=True)
                recognized_text = recognizer.recognize_google(audio).lower()  # Convert to lowercase
                if recognized_text:
                    translated_text = translation_hin_to_eng(recognized_text)
                    print("\rMr.Stank: " + translated_text)
                    return translated_text  # Return the translated text
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_text = ""  # Set recognized_text to an empty string in case of error
            finally:
                print("\r", end='', flush=True)  # Erase "Listening...." and "Recognizing..."
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console after recognition


            listen_thread = threading.Thread(target=listen)
            listen_thread.start()
            print_thread = threading.Thread(target=print_loop)
            print_thread.start()

            listen_thread.join()
            print_thread.join()


