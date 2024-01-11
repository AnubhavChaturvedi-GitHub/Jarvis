import psutil
import time
from Body.speak import speak
from playsound import playsound


def battery_alert():
    while True:
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            speak("sir,your device is running very low battery. please charge it")

        elif percent < 10:
            speak("sir,this is last chance. your battery is very low")

        elif percent == 100:
            speak(
                "sir, Battery is running on 100 percent full  battery power, And I think it's fully charged ,"
                "please unplug it")
        else:
            pass

        time.sleep(1500)


def battey_persentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)

    speak(f"the device is running on {percent}% battery power")


def check_plugin_status():
    battery = psutil.sensors_battery()
    previous_state = battery.power_plugged

    while True:
        battery = psutil.sensors_battery()

        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                speak("plugging successfully your device is charging now")
            else:
                speak("Your device is plugged out now you're running on your battery power")

            previous_state = battery.power_plugged

        time.sleep(1)
