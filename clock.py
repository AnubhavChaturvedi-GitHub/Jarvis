import datetime
import time
from Body.speak import speak
from Works.wish import *



def set_alarm(alarm_time_str):
    try:
        alarm_time = datetime.datetime.strptime(alarm_time_str, "%I:%M %p").time()
        current_time = datetime.datetime.now().time()

        while current_time < alarm_time:
            time.sleep(1)  # Avoid busy-waiting, sleep for a short duration
            current_time = datetime.datetime.now().time()
            break

        wish()


    except ValueError:
        error_message = "Sir, this is an invalid time format. Please use the format like '8:00 AM'."
        print(error_message)
        speak(error_message)


def what_is_the_time():
    try:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    except Exception as e:
        error_message = f"An error occurred: {e}"
        print(error_message)
        speak(error_message)


