import os
import pyautogui
from Body.listen import hearing
from Body.speak import speak


def take_screenshot():
    # Define the directory path
    directory_path = r"C:\Users\vlogp\Desktop\J.A.R.V.I.S\Database\imagedata"

    # Check if the directory exists; if not, create it
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Ask the user for the screenshot file name
    speak("What would you like to name the screenshot file?")
    name = hearing()

    # Validate the input and append the correct file extension (.jpg)
    if not name.endswith(".jpg"):
        name += ".jpg"

    # Save the screenshot to a file with the correct file extension (.jpg)
    screenshot_path = os.path.join(directory_path, name)
    screenshot.save(screenshot_path, format="JPEG")

    speak(f"Screenshot successfully saved as {name} in database folder")

