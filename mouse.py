import pyautogui
import time

def click_at_position(x, y):
    # Move the mouse to the specified position
    pyautogui.moveTo(x, y, duration=0.1)

    # Perform a left mouse click
    pyautogui.click()

# Example usage: Click at coordinates (100, 100)

