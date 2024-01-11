import subprocess
import time

import pyautogui as gui



def open_pycharm():
    gui.press("win")
    time.sleep(1)
    gui.write("pycharm")
    time.sleep(1)
    gui.press("enter")


def open_whatsapp():
    gui.press("win")
    time.sleep(1)
    gui.write("whatsapp")
    time.sleep(1)
    gui.press("enter")



def open_linkedin():
    gui.press("win")
    time.sleep(1)
    gui.write("linkedin")
    time.sleep(1)
    gui.press("enter")


def open_edge():
    gui.press("win")
    time.sleep(1)
    gui.write("edge")
    time.sleep(1)
    gui.press("enter")


def open_spotify():
    gui.press("win")
    time.sleep(1)
    gui.write("spotify")
    time.sleep(1)
    gui.press("enter")


def open_settings():
    gui.press("win")
    time.sleep(1)
    gui.write("settings")
    time.sleep(1)
    gui.press("enter")


def open_microsoft_store():
    gui.press("win")
    time.sleep(1)
    gui.write("microsoftstore")
    time.sleep(1)
    gui.press("enter")

def open_photos():
    gui.press("win")
    time.sleep(1)
    gui.write("photos")
    time.sleep(1)
    gui.press("enter")

def open_paint():
    gui.press("win")
    time.sleep(1)
    gui.write("paint")
    time.sleep(1)
    gui.press("enter")

def open_control_panel():
    gui.press("win")
    time.sleep(1)
    gui.write("control panel")
    time.sleep(1)
    gui.press("enter")

def open_word():
    gui.press("win")
    time.sleep(1)
    gui.write("officesuite d")
    time.sleep(1)
    gui.press("enter")

def open_pdfreader():
    gui.press("win")
    time.sleep(1)
    gui.write("officesuite p")
    time.sleep(1)
    gui.press("enter")

def open_powerpoind():
    gui.press("win")
    time.sleep(1)
    gui.write("officesuite slides")
    time.sleep(1)
    gui.press("enter")

def open_wpsoffice():
    gui.press("win")
    time.sleep(1)
    gui.write("wps office")
    time.sleep(1)
    gui.press("enter")

def open_pycharm():
    run_command("pycharm")

def run_command(command):
    try:
        # Run the command in the background
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        time.sleep(2)  # Wait for the command prompt to start (adjust as needed)

        # Send a command to the command prompt
        command_to_send = "your_command_here\n"
        process.stdin.write(command_to_send.encode('utf-8'))
        process.stdin.flush()

        # Optionally, you can read the output
        output, error = process.communicate()
        print("Output:", output.decode('utf-8'))
        print("Error:", error.decode('utf-8'))

    except Exception as e:
        print("Error:", e)

def open_cursor():
    run_command("cursor")
