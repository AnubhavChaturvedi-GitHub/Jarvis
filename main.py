import pygame
from pywhatkit.core.core import send_message
from Works.clock import *
from Works.battery import *
from Works.brain import *
from Works.open_operation import *
from Works.Youtube import *
from Works.Study_Time_Activated import *
from Works.WhatsApp_Automation import *
from Works.spotify import *
from Works.speed_test import *
from Works.openapp import *
from Works.search import *
from Works.check_map import *
from Works.news import news
from Works.location import *
from Works.screenshort import *
from Works.reminder import *
import keyboard
from Works.scroll import *
from Works.yt_test import play_song
from Works.WelcomeRandom import *
from Works.alam import *
from Advance.project import *
from Works.summary import *



operation_dict = {
    "open wps office": open_wpsoffice,
    "open python code editor": open_pycharm,
    "open business whatsapp": open_whatsapp,
    "open linkedin app": open_linkedin,
    "open browser": open_edge,
    "open spotify": open_spotify,
    "open settings": open_settings,
    "open Microsoft store": open_microsoft_store,
    "open paint": open_paint,
    "open photos": open_photos,
    "open ms word": open_word,
    "open powerpoint": open_powerpoind,
    "open pdf reader": open_pdfreader,
    "open control panel": open_control_panel,
}
qa_file_path = "C:\\Users\\vlogp\\Desktop\\J.A.R.V.I.S\\Database\\qna_logbook.txt"
qa_dict = load_qa_data(qa_file_path)

number_mapping = {
    'first': '1',
    'second': '2',
    'third': '3',
    'fourth': '4',
    'fifth': '5',
    'sixth': '6',
    'seventh': '7',
    'eighth': '8',
    'ninth': '9',
    'tenth': '10'
}

def main():
 while True:
    wakeup = hearing().lower()
    if "wakeup" in wakeup or "wake up" in wakeup or "wake up jarvis" in wakeup or "jago jarvis" in wakeup or "jarvis" in wakeup or "jarvis jago" in wakeup or "jarvis is there" in wakeup or "jarvis there" in wakeup or "jarvis ya there" in wakeup:
     print("⚡⚡⚡⚡⚡⚡⚡⚡⚡-F.R.I.D.A.Y-⚡⚡⚡⚡⚡⚡⚡⚡⚡")
     welcome()

     no_input_count = 0
     while True:
        text = hearing()
        text = text.strip ()
        text = text.replace("big","open")

        if not text:
            no_input_count += 1

            if no_input_count == 10 :
                print("<<<<<<<<F.R.I.D.A.Y---(Sleeping).>>>>>>>>>")
                speak("Sir, I think I should go to sleep for some time")
                main()
                break

        else:
            no_input_count = 0
            if "waqt kya hai" in text or "samay kya hai" in text or "kitne baje hain" in text or "kitna samay hua" in text or "what is the time" in text or "what time is it" in text:
                what_is_the_time()
                pass

            elif text.startswith(("kaun hai", "kya hai", "kaise kare", "kya hote hain", "dikhao", "batado", "bataye", "ka naam suna hai", "suna hai","what is","who is","who are","what are","how to")):
                search_brain(text)

            elif text.startswith(("who is ", "what is ", "how to ", "what are", " show me", "tell me", "tell me about","what"
                                  "ka naam suna hai", "is heard")):
                search_brain(text)

            elif "set alarm" in text or "set alarm a.m." in text or "set alarm p.m." in text or "jarvis set alarm" in text:
                alam(text)

            elif "open youtube studio" in text or "open YouTube studio" in text or "open youtube studio" in text or "open youtube studio" in text or "khologe youtube studio" in text or "youtube studio kholo" in text or "youtube studio khologe" in text:
                open_ytstudio()

            elif "summarize it" in text or "summary karo" in text or "summary karoge" in text:
                speak("chuld you please enter the paragraph")
                text = input()
                summary(text)

            elif "open google classroom using college id" in text or " open Google classroom using collage i d" in text or "open collage classroom" in text or "open classroom using collage id" in text or "classroom kholo collage id se" in text or "big classroom" in text or "google classroom kholo" in text or "classroom size" in text:
                open_googleclassroom_default1()

            elif "open google classroom" in text or " open Google classroom" in text or "open google classroom" in text or "open google classroom" in text or "classroom kholo" in text or "big classroom" in text or "google classroom kholo" in text or "classroom size" in text:
                open_googleclassroom_default()



            elif "open facebook" in text or "open Facebook" in text or "open faceboo" in text or "open facebook" in text or "big facebook" in text :
                open_facebook()

            elif "check battery percentage" in text or "check battery" in text or "check battey persent" in text or "check battery" in text or "how much battery" in text:
                battey_persentage()

            elif "open youtube" in text or "open tube " in text or "youtube khologe" in text:
                open_youtube()

            elif "open telegram" in text or "open telegram app" in text:
                open_telegram()

            elif "open instagram" in text or "open insta" in text or "instagram khologe" in text:
                open_insta()

            elif "open chrome" in text or "open google" in text or "google khologe" in text or "google kholo" in text:
                open_chrome()

            elif "open whatsapp" in text or "open what'sapp" in text or "open whats app" in text or "open what's app" in text or "what's app kholo" in text or "whatsapp khologe" in text or "WhatsApp is great" in text:
                open_Whatsapp()

            elif "open chat GPT" in text or "open chatgpt" in text or "open chat gpt" in text or "open chat gpt" in text or "chat gpt kholo" in text:
                open_chat_GPT()

            elif "close tab" in text or "close current tab" in text or "close this tab" in text:
                speak("Closing Current Tab.")
                gui.hotkey("ctrl", "w")

            elif "close" in text or "close this" in text  or "band kar do" in text:
                speak("closing...")
                gui.hotkey('alt', 'f4')

            elif text in qa_dict:
                ans = qa_dict[text]
                speak_thread = threading.Thread(target=speak, args=(ans,))
                speak_thread.start()
                speak_thread.join()

            elif "shutdown" in text or "shut down" in text:
                speak("ok say ! good bye")
                shut_down()

            elif "restart" in text or "re start" in text:
                speak("start the pc refreshing system")
                restart()


            elif "good morning" in text or "good evening" in text:
                wish()

            elif "minimise" in text or "minimise the window" in text or "minimize karoge" in text or "minimize karo" in text:
                speak("minimizing..")
                gui.hotkey('win', 'down')
                gui.hotkey('win', 'down')

            elif "minimise" in text or "minimise the window" in text or "hata do" in text or "it will be do" in text :
                gui.hotkey('win', 'down')
                gui.hotkey('win', 'down')

            elif "play music" in text:
                 speak("Sir, where would you like to play music? YouTube or Spotify?")
                 platform_choice = hearing()
                 if "youtube" in platform_choice:
                          speak("Sir, which song do you want to play on YouTube?")
                          song_name = hearing()
                          play_song(song_name)
                 elif "spotify" in platform_choice:
                            playmusics()

            elif "send message on whatsapp" in text:
                speak("well,who is that great person")
                text = hearing()
                if "girlfriend" in text or "my girlfriend" in text:
                    text = "shejal"
                    speak("ok mr stank , what should i send")
                    message = hearing()
                    send_message(text,message)
                    gui.hotkey("alt","f4")
                    speak(f"Done ! i have successfully send the massege {message} to your girlfriend")
                else:
                    speak("ok mr stank , what should i send")
                    message = hearing()
                    send_message(text,message)
                    gui.hotkey("alt","f4")
                    speak(f"Done ! i have successfully send the massege {message} to {text}")

            elif "whatsapp call" in text or "whats app call" in text or "call karoge" in text :
                speak("sure ! who is the lucky one")
                name = hearing()
                if "girlfriend" in text or "my girlfriend" in name:
                    text = "shejal"
                    speak("which call sir ! video or audio")
                    message = hearing()
                    send_message(text, message)
                    gui.hotkey("alt", "f4")
                    speak("done sir")
                whatsapp_call(name)


            elif "jarvis" in text:
                search_brain(text)

            elif "good night" in text:
                good_night_setup()

            elif "i want to study" in text or "study time" in text or "study setup activated" in text:
                study_time_setup()

            elif text in operation_dict:
                text = text.replace("open", "opening")
                speak(text)
                text = text.replace("opening", "open")
                operation_dict[text]()


            elif "search in google" in text or "search on google" in text or "google me search kao" in text or "google search" in text or "search in internet" in text:
                text = text.replace("search in google", "")
                text = text.replace("search on google", "")
                print(f"searching{text} on internet")
                speak(f"searching{text} on internet")
                search_on_google(text)

            elif "search in youtube" in text or "search on youtube" in text or "youtube per search karo" in text:
                text = text.replace("search in youtube", "")
                text = text.replace("search on youtube", "")
                print(f"searching{text} on youtube")
                speak(f"searching{text} on youtube")
                search_on_youtube(text)

            elif "search in chatgpt" in text or "search on chatgpt" in text or "search in chat gpt" in text or "search on chat gpt" in text or "ask to jarvis" in text or "ask jarvis" in text:
                text = text.replace("search in chatgpt", "")
                text = text.replace("search on chatgpt", "")
                text = text.replace("search in chat gpt", "")
                text = text.replace("search on chat gpt", "")
                text = text.replace("ask to jarvis", "")
                text = text.replace("ask jarvis", "")

                search_on_chatgpt(text)


            elif "write" in text or "likho" in text or "right" in text:
                speak("writing")
                text = text.replace("write", "").replace("likho", "").replace("right", "")
                gui.write(text)

            elif "enter" in text or "press enter" in text or "send" in text:
                gui.press("enter")

            elif "select all" in text or 'select all paragraph' in text:
                gui.hotkey("ctrl","a")

            elif "copy" in text or 'copy this' in text:
                gui.hotkey("ctrl","c")

            elif "paste" in text or 'paste here' in text:
                gui.hotkey("ctrl","v")

            elif "undo" in text or 'undo karo' in text:
                gui.hotkey("ctrl","z")

            elif "copy last paragraph" in text:
                gui.hotkey("ctrl", "shift", "c")

            elif "increase volume" in text or "volume badhao" in text or "increase the volume" in text:
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                print("Volume increased.")
            elif "decrease volume" in text or "volume kam karo" in text or "decrease the volume" in text:
                gui.press("volumedown")
                gui.press("volumedown")
                gui.press("volumedown")
                gui.press("volumedown")
                gui.press("volumedown")
                speak("Volume decreased.")
                print("Volume decreased.")

            elif "full volume" in text or "full volume kr do" in text :
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                gui.press("volumeup")
                speak("now your system in full volume")
                print("now your system in full volume")

            elif "mute" in text:
                gui.press("volumemute")
                print("Volume muted.")

            elif "check internet speed" in text or "check speed" in text :
                check_internet_speed()

            elif "show me the location" in text or "check location" in text or "where is" in text:
                text = text.replace("show me the location","")
                text =text.replace("check location","")
                text = text.replace("where is","")
                map(text)

            elif "take some rest" in text or "go to sleep" in text or "so jao jarvis" in text:
                speak("ok sir ! call me any time again")
                main()

            elif "news" in text or "tell me top 5 news" in text or "todays news" in text:
                news()

            elif "where i am" in text or "where we are" in text:
               speak("let me check.. ")
               get_current_location()

            elif "take screenshot" in text or "screenshot it" in text:
               speak("ok taking..")
               take_screenshot()

            elif "visit" in text:
              Nameofweb = text.replace("visit ","")
              speak(f"visiting {Nameofweb}")
              Link = f"https://www.{Nameofweb}.com"
              webbrowser.open(Link)

            elif "launch" in text:
                Nameofweb = text.replace("launch ","")
                speak(f"launching {Nameofweb}")
                Link = f"https://www.{Nameofweb}.com"
                webbrowser.open(Link)


            elif "make pending work list" in text or "make list for work" in text or "add work in list" in text or "ad in work list" in text:
                logic()

            elif "today pending works" in text or "show me pending work list" in text or "pending work dikhao" in text or "pending work kya hai" in text:
                remind_pending_works()
                speak("Sir, have you done any work?")
                index_text = hearing().lower()

                if "clear all" in index_text:
                    # Clear all content from the files
                    with open('reminders.txt', 'w'):
                        pass
                    with open('pending_works.txt', 'w'):
                        pass
                    speak("All files cleared.")
                else:
                    for word, number_str in number_mapping.items():
                        if word in index_text:
                            index_text = index_text.replace(word, number_str)

                    try:
                        index = int(index_text)
                        # Now 'index' should contain the numeric value corresponding to the word
                        if 1 <= index <= 10:
                            remove_pending_work(index - 1)  # Adjusting for 1-based indexing
                            speak(f"Great! You've completed the {number_mapping.get(index_text, 'task')}.")
                        else:
                            speak("Sorry, the task number is out of range.")
                    except ValueError:
                        speak("Sorry, I couldn't understand which task you completed.")

            elif "open code editor for python" in text or "open python code editor" in text or "open python code editor" in text:
                speak("opening..,python code editor")
                open_pycharm()

            elif "open advance code editor" in text or "open code editor" in text or "code editor" in text:
                speak("opening..,code editor")
                open_cursor()

            elif "scroll up" in text :
                scrool_up()

            elif "scroll down" in text:
                scroll_down()

            elif "play" in text or "pause" in text or "stop" in text:
                ui.hotkey("space")

            elif text.startswith("search"):
                gui.hotkey("/")
                text = text.replace("search","")
                gui.write(text)
                time.sleep(3)
                gui.press("enter")
                speak(f"searching {text}")
                print(f"searching {text}")

            elif "open ease of access center" in text or "ease of access center" in text:
                speak("Opening Ease of Access Center.")
                os.system("control access.cpl")

            # Example 2
            elif "open region and language settings" in text or "region and language" in text:
                speak("Opening Region and Language Settings.")
                os.system("control intl.cpl")

            # Example 3
            elif "open user accounts" in text or "user accounts" in text:
                speak("Opening User Accounts.")
                os.system("control userpasswords2")

            # Example 4
            elif "open display adapter settings" in text or "display adapter" in text:
                speak("Opening Display Adapter Settings.")
                os.system("control desktop")

            # Example 5
            elif "open network and sharing center" in text or "network sharing" in text:
                speak("Opening Network and Sharing Center.")
                os.system("control.exe /name Microsoft.NetworkAndSharingCenter")

            # Example 6
            elif "open Windows Defender settings" in text or "Windows Defender" in text:
                speak("Opening Windows Defender Settings.")
                os.system("start ms-settings:windowsdefender")

            # Example 7
            elif "open system properties" in text or "system properties" in text:
                speak("Opening System Properties.")
                os.system("sysdm.cpl")

            # Example 8
            elif "open device manager" in text or "device manager" in text:
                speak("Opening Device Manager.")
                os.system("devmgmt.msc")

            # Example 9
            elif "open power options" in text or "power options" in text:
                speak("Opening Power Options.")
                os.system("powercfg.cpl")

            # Example 10
            elif "open sound settings" in text or "sound settings" in text:
                speak("Opening Sound Settings.")
                os.system("mmsys.cpl")

            # Example 11
            elif "open system configuration" in text or "system configuration" in text:
                speak("Opening System Configuration.")
                os.system("msconfig")

            # Example 12
            elif "open firewall settings" in text or "firewall settings" in text:
                speak("Opening Firewall Settings.")
                os.system("control firewall.cpl")

            # Example 13
            elif "open Bluetooth settings" in text or "Bluetooth settings" in text:
                speak("Opening Bluetooth Settings.")
                os.system("fsquirt")

            # Example 14
            elif "open keyboard settings" in text or "keyboard settings" in text:
                speak("Opening Keyboard Settings.")
                os.system("control keyboard")

            # Example 15
            elif "open mouse settings" in text or "mouse settings" in text:
                speak("Opening Mouse Settings.")
                os.system("control mouse")

            # Example 16
            elif "open date and time settings" in text or "date and time" in text:
                speak("Opening Date and Time Settings.")
                os.system("control timedate.cpl")

            # Example 17
            elif "open task manager" in text or "task manager" in text:
                speak("Opening Task Manager.")
                os.system("taskmgr")

            # Example 18
            elif "open system monitor" in text or "system monitor" in text:
                speak("Opening System Monitor.")
                os.system("perfmon")

            # Example 19
            elif "open disk cleanup" in text or "disk cleanup" in text:
                speak("Opening Disk Cleanup.")
                os.system("cleanmgr")

            # Example 20
            elif "open remote desktop" in text or "remote desktop" in text:
                speak("Opening Remote Desktop.")
                os.system("mstsc")

            # Add more examples as needed
            # Example 21
            elif "open control panel" in text or "control panel" in text:
                speak("Opening Control Panel.")
                os.system("control")

            # Example 22
            elif "open system update settings" in text or "system update" in text:
                speak("Opening System Update Settings.")
                os.system("ms-settings:windowsupdate")

            # Example 23
            elif "open disk management" in text or "disk management" in text:
                speak("Opening Disk Management.")
                os.system("diskmgmt.msc")

            # Example 24
            elif "open environment variables" in text or "environment variables" in text:
                speak("Opening Environment Variables.")
                os.system("systempropertiesadvanced")

            # Example 25
            elif "open system information" in text or "system information" in text:
                speak("Opening System Information.")
                os.system("msinfo32")

            # Example 26
            elif "open programs and features" in text or "programs and features" in text:
                speak("Opening Programs and Features.")
                os.system("appwiz.cpl")

            # Example 27
            elif "open display settings" in text or "display settings" in text:
                speak("Opening Display Settings.")
                os.system("ms-settings:display")

            # Example 28
            elif "open network adapters" in text or "network adapters" in text:
                speak("Opening Network Adapters.")
                os.system("ncpa.cpl")

            # Example 29
            elif "open advanced system settings" in text or "advanced system settings" in text:
                speak("Opening Advanced System Settings.")
                os.system("systempropertiesadvanced")

            # Example 30
            elif "open default programs" in text or "default programs" in text:
                speak("Opening Default Programs.")
                os.system("control /name Microsoft.DefaultPrograms")

            # Add more examples as needed
            # Example 31
            elif "open power plan settings" in text or "power plan" in text:
                speak("Opening Power Plan Settings.")
                os.system("powercfg.cpl")

            # Example 32
            elif "open device and printers" in text or "device and printers" in text:
                speak("Opening Devices and Printers.")
                os.system("control printers")

            # Example 33
            elif "open system restore" in text or "system restore" in text:
                speak("Opening System Restore.")
                os.system("rstrui.exe")

            # Example 34
            elif "open Windows features" in text or "Windows features" in text:
                speak("Opening Windows Features.")
                os.system("optionalfeatures")

            # Example 35
            elif "open language preferences" in text or "language preferences" in text:
                speak("Opening Language Preferences.")
                os.system("ms-settings:regionlanguage")

            # Example 36
            elif "open credential manager" in text or "credential manager" in text:
                speak("Opening Credential Manager.")
                os.system("control /name Microsoft.CredentialManager")

            # Example 37
            elif "open system configuration" in text or "system configuration" in text:
                speak("Opening System Configuration.")
                os.system("msconfig")

            # Example 38
            elif "open system properties" in text or "system properties" in text:
                speak("Opening System Properties.")
                os.system("sysdm.cpl")

            # Example 39
            elif "open task scheduler" in text or "task scheduler" in text:
                speak("Opening Task Scheduler.")
                os.system("taskschd.msc")

            # Example 40
            elif "open file explorer" in text or "file explorer" in text:
                speak("Opening File Explorer.")
                os.system("explorer")

            # Add more examples as needed
            # Example 41
            elif "open remote settings" in text or "remote settings" in text:
                speak("Opening Remote Settings.")
                os.system("ms-settings:remotedesktop")

            # Example 42
            elif "open disk properties" in text or "disk properties" in text:
                speak("Opening Disk Properties.")
                os.system("diskpart")

            # Example 43
            elif "open environment variables" in text or "environment variables" in text:
                speak("Opening Environment Variables.")
                os.system("rundll32.exe sysdm.cpl,EditEnvironmentVariables")

            # Example 44
            elif "open color management" in text or "color management" in text:
                speak("Opening Color Management.")
                os.system("colorcpl")

            # Example 45
            elif "open system cleanup" in text or "system cleanup" in text:
                speak("Opening System Cleanup.")
                os.system("cleanmgr /sageset:1")

            # Example 46
            elif "open display calibration" in text or "display calibration" in text:
                speak("Opening Display Calibration.")
                os.system("dccw")

            # Example 47
            elif "open backup and restore" in text or "backup and restore" in text:
                speak("Opening Backup and Restore.")
                os.system("sdclt")

            # Example 48
            elif "open network connections" in text or "network connections" in text:
                speak("Opening Network Connections.")
                os.system("control netconnections")

            # Example 49
            elif "open sound mixer" in text or "sound mixer" in text:
                speak("Opening Sound Mixer.")
                os.system("sndvol")

            # Example 50
            elif "open device installation settings" in text or "device installation" in text:
                speak("Opening Device Installation Settings.")
                os.system("ms-settings:windowsupdate-deviceoptions")

            # Add more examples as needed
            # Example 51
            elif "open Windows features" in text or "Windows features" in text:
                speak("Opening Windows Features.")
                os.system("optionalfeatures")

            # Example 52
            elif "open display settings" in text or "display settings" in text:
                speak("Opening Display Settings.")
                os.system("ms-settings:display")

            # Example 53
            elif "open system information" in text or "system information" in text:
                speak("Opening System Information.")
                os.system("msinfo32")

            # Example 54
            elif "open disk cleanup" in text or "disk cleanup" in text:
                speak("Opening Disk Cleanup.")
                os.system("cleanmgr")

            # Example 55
            elif "open remote desktop" in text or "remote desktop" in text:
                speak("Opening Remote Desktop.")
                os.system("mstsc")

            # Example 56
            elif "open control panel" in text or "control panel" in text:
                speak("Opening Control Panel.")
                os.system("control")

            # Example 57
            elif "open system update settings" in text or "system update" in text:
                speak("Opening System Update Settings.")
                os.system("ms-settings:windowsupdate")

            # Example 58
            elif "open disk management" in text or "disk management" in text:
                speak("Opening Disk Management.")
                os.system("diskmgmt.msc")

            # Example 59
            elif "open environment variables" in text or "environment variables" in text:
                speak("Opening Environment Variables.")
                os.system("systempropertiesadvanced")

            # Example 60
            elif "open system information" in text or "system information" in text:
                speak("Opening System Information.")
                os.system("msinfo32")

            # Add more examples as needed
            # Example 61
            elif "open program and features" in text or "programs and features" in text:
                speak("Opening Programs and Features.")
                os.system("appwiz.cpl")

            # Example 62
            elif "open device and printers" in text or "devices and printers" in text:
                speak("Opening Devices and Printers.")
                os.system("control printers")

            # Example 63
            elif "open system restore" in text or "system restore" in text:
                speak("Opening System Restore.")
                os.system("rstrui.exe")

            # Example 64
            elif "open Windows security" in text or "Windows security" in text:
                speak("Opening Windows Security.")
                os.system("ms-settings:windowsdefender")

            # Example 65
            elif "open date and time settings" in text or "date and time" in text:
                speak("Opening Date and Time Settings.")
                os.system("control timedate.cpl")

            # Example 66
            elif "open task manager" in text or "task manager" in text:
                speak("Opening Task Manager.")
                os.system("taskmgr")

            # Example 67
            elif "open system monitor" in text or "system monitor" in text:
                speak("Opening System Monitor.")
                os.system("perfmon")

            # Example 68
            elif "open device manager" in text or "device manager" in text:
                speak("Opening Device Manager.")
                os.system("devmgmt.msc")

            # Example 69
            elif "open power options" in text or "power options" in text:
                speak("Opening Power Options.")
                os.system("powercfg.cpl")

            # Example 70
            elif "open sound settings" in text or "sound settings" in text:
                speak("Opening Sound Settings.")
                os.system("mmsys.cpl")

            # Add more examples as needed
            # Example 71
            elif "open network and sharing center" in text or "network sharing" in text:
                speak("Opening Network and Sharing Center.")
                os.system("control.exe /name Microsoft.NetworkAndSharingCenter")

            # Example 72
            elif "open Windows Defender settings" in text or "Windows Defender" in text:
                speak("Opening Windows Defender Settings.")
                os.system("start ms-settings:windowsdefender")

            # Example 73
            elif "open system configuration" in text or "system configuration" in text:
                speak("Opening System Configuration.")
                os.system("msconfig")

            # Example 74
            elif "open firewall settings" in text or "firewall settings" in text:
                speak("Opening Firewall Settings.")
                os.system("control firewall.cpl")

            # Example 75
            elif "open Bluetooth settings" in text or "Bluetooth settings" in text:
                speak("Opening Bluetooth Settings.")
                os.system("fsquirt")

            # Example 76
            elif "open keyboard settings" in text or "keyboard settings" in text:
                speak("Opening Keyboard Settings.")
                os.system("control keyboard")

            # Example 77
            elif "open mouse settings" in text or "mouse settings" in text:
                speak("Opening Mouse Settings.")
                os.system("control mouse")

            # Example 78
            elif "open region and language settings" in text or "region and language" in text:
                speak("Opening Region and Language Settings.")
                os.system("control intl.cpl")

            # Example 79
            elif "open user accounts" in text or "user accounts" in text:
                speak("Opening User Accounts.")
                os.system("control userpasswords2")

            # Example 80
            elif "open system properties" in text or "system properties" in text:
                speak("Opening System Properties.")
                os.system("sysdm.cpl")

            # Add more examples as needed
            # Example 81
            elif "open taskbar settings" in text or "taskbar settings" in text:
                speak("Opening Taskbar Settings.")
                os.system("ms-settings:taskbar")

            # Example 82
            elif "open Windows update history" in text or "update history" in text:
                speak("Opening Windows Update History.")
                os.system("ms-settings:windowsupdate-history")

            # Example 83
            elif "open system reliability monitor" in text or "reliability monitor" in text:
                speak("Opening System Reliability Monitor.")
                os.system("perfmon /rel")

            # Example 84
            elif "open system performance settings" in text or "performance settings" in text:
                speak("Opening Performance Settings.")
                os.system("systempropertiesperformance")

            # Example 85
            elif "open system privacy settings" in text or "privacy settings" in text:
                speak("Opening Privacy Settings.")
                os.system("ms-settings:privacy")

            # Example 86
            elif "open system storage settings" in text or "storage settings" in text:
                speak("Opening Storage Settings.")
                os.system("ms-settings:storagesense")

            # Example 87
            elif "open system update check" in text or "update check" in text:
                speak("Checking for System Updates.")
                os.system("ms-settings:windowsupdate-action")

            # Example 88
            elif "open system screen settings" in text or "screen settings" in text:
                speak("Opening Screen Settings.")
                os.system("ms-settings:display")

            # Example 89
            elif "open system power plan" in text or "power plan" in text:
                speak("Opening Power Plan Settings.")
                os.system("powercfg.cpl")

            # Example 90
            elif "open system user accounts" in text or "user accounts" in text:
                speak("Opening User Accounts.")
                os.system("netplwiz")

            # Add more examples as needed
            # Example 91
            elif "open system sound settings" in text or "sound settings" in text:
                speak("Opening Sound Settings.")
                os.system("mmsys.cpl")

            # Example 92
            elif "open system privacy dashboard" in text or "privacy dashboard" in text:
                speak("Opening Privacy Dashboard.")
                os.system("ms-settings:privacy-feedback")

            # Example 93
            elif "open system screen saver settings" in text or "screen saver settings" in text:
                speak("Opening Screen Saver Settings.")
                os.system("control desk.cpl,screensaver,@screensaver")

            # Example 94
            elif "open system network adapters" in text or "network adapters" in text:
                speak("Opening Network Adapters.")
                os.system("ncpa.cpl")

            # Example 95
            elif "open system game mode settings" in text or "game mode settings" in text:
                speak("Opening Game Mode Settings.")
                os.system("ms-settings:gaming-gamemode")

            # Example 96
            elif "open system privacy diagnostics" in text or "privacy diagnostics" in text:
                speak("Opening Privacy Diagnostics.")
                os.system("ms-settings:privacy-diagnostics")

            # Example 97
            elif "open system region and language settings" in text or "region and language" in text:
                speak("Opening Region and Language Settings.")
                os.system("control intl.cpl")

            # Example 98
            elif "open system display color calibration" in text or "display color calibration" in text:
                speak("Opening Display Color Calibration.")
                os.system("dccw")

            # Example 99
            elif "open system recovery" in text or "system recovery" in text:
                speak("Opening System Recovery.")
                os.system("control.exe /name Microsoft.Recovery")

            # Example 100
            elif "open system DirectX diagnostic tool" in text or "DirectX diagnostic tool" in text:
                speak("Opening DirectX Diagnostic Tool.")
                os.system("dxdiag")

            # Add more examples as needed
            # Example 101
            elif "close control panel" in text or "control panel close" in text:
                speak("Closing Control Panel.")
                os.system("taskkill /im control.exe")

            # Example 102
            elif "close task manager" in text or "task manager close" in text:
                speak("Closing Task Manager.")
                os.system("taskkill /im taskmgr.exe")

            # Example 103
            elif "close system configuration" in text or "system configuration close" in text:
                speak("Closing System Configuration.")
                os.system("taskkill /im msconfig.exe")

            # Example 104
            elif "close command prompt" in text or "command prompt close" in text:
                speak("Closing Command Prompt.")
                os.system("taskkill /im cmd.exe")

            # Example 105
            elif "close notepad" in text or "notepad close" in text:
                speak("Closing Notepad.")
                os.system("taskkill /im notepad.exe")

            # Example 106
            elif "close file explorer" in text or "file explorer close" in text:
                speak("Closing File Explorer.")
                os.system("taskkill /im explorer.exe")

            # Example 107
            elif "close Windows security" in text or "Windows security close" in text:
                speak("Closing Windows Security.")
                os.system("taskkill /im WindowsSecurity.exe")

            # Example 108
            elif "close remote desktop" in text or "remote desktop close" in text:
                speak("Closing Remote Desktop.")
                os.system("taskkill /im mstsc.exe")

            # Example 109
            elif "close control firewall" in text or "firewall close" in text:
                speak("Closing Firewall Settings.")
                os.system("taskkill /im firewall.cpl")

            # Example 110
            elif "close system monitor" in text or "system monitor close" in text:
                speak("Closing System Monitor.")
                os.system("taskkill /im perfmon.exe")

            # Add more examples as needed
            # Example 111
            elif "close ease of access center" in text or "ease of access center close" in text:
                speak("Closing Ease of Access Center.")
                os.system("taskkill /im access.cpl")

            # Example 112
            elif "close region and language settings" in text or "region and language close" in text:
                speak("Closing Region and Language Settings.")
                os.system("taskkill /im intl.cpl")

            # Example 113
            elif "close user accounts" in text or "user accounts close" in text:
                speak("Closing User Accounts.")
                os.system("taskkill /im userpasswords2.exe")

            # Example 114
            elif "close display adapter settings" in text or "display adapter close" in text:
                speak("Closing Display Adapter Settings.")
                os.system("taskkill /im rundll32.exe")

            # Example 115
            elif "close network and sharing center" in text or "network sharing close" in text:
                speak("Closing Network and Sharing Center.")
                os.system("taskkill /im explorer.exe")

            # Example 116
            elif "close Windows Defender settings" in text or "Windows Defender close" in text:
                speak("Closing Windows Defender Settings.")
                os.system("taskkill /im WindowsDefender.exe")

            # Example 117
            elif "close system properties" in text or "system properties close" in text:
                speak("Closing System Properties.")
                os.system("taskkill /im sysdm.cpl")

            # Example 118
            elif "close device manager" in text or "device manager close" in text:
                speak("Closing Device Manager.")
                os.system("taskkill /im devmgmt.msc")

            # Example 119
            elif "close power options" in text or "power options close" in text:
                speak("Closing Power Options.")
                os.system("taskkill /im powercfg.cpl")

            # Example 120
            elif "close sound settings" in text or "sound settings close" in text:
                speak("Closing Sound Settings.")
                os.system("taskkill /im mmsys.cpl")

            # Add more examples as needed
            # Example 121
            elif "close control panel" in text or "control panel close" in text:
                speak("Closing Control Panel.")
                os.system("taskkill /im control.exe")

            # Example 122
            elif "close system update settings" in text or "system update close" in text:
                speak("Closing System Update Settings.")
                os.system("taskkill /im ms-settings:windowsupdate")

            # Example 123
            elif "close disk management" in text or "disk management close" in text:
                speak("Closing Disk Management.")
                os.system("taskkill /im diskmgmt.msc")

            # Example 124
            elif "close environment variables" in text or "environment variables close" in text:
                speak("Closing Environment Variables.")
                os.system("taskkill /im rundll32.exe")

            # Example 125
            elif "close system information" in text or "system information close" in text:
                speak("Closing System Information.")
                os.system("taskkill /im msinfo32.exe")

            # Example 126
            elif "close programs and features" in text or "programs and features close" in text:
                speak("Closing Programs and Features.")
                os.system("taskkill /im appwiz.cpl")

            # Example 127
            elif "close display settings" in text or "display settings close" in text:
                speak("Closing Display Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 128
            elif "close network adapters" in text or "network adapters close" in text:
                speak("Closing Network Adapters.")
                os.system("taskkill /im ncpa.cpl")

            # Example 129
            elif "close advanced system settings" in text or "advanced system settings close" in text:
                speak("Closing Advanced System Settings.")
                os.system("taskkill /im rundll32.exe")

            # Example 130
            elif "close default programs" in text or "default programs close" in text:
                speak("Closing Default Programs.")
                os.system("taskkill /im control.exe")

            # Add more examples as needed
            # Example 131
            elif "close power plan settings" in text or "power plan close" in text:
                speak("Closing Power Plan Settings.")
                os.system("taskkill /im powercfg.cpl")

            # Example 132
            elif "close devices and printers" in text or "devices and printers close" in text:
                speak("Closing Devices and Printers.")
                os.system("taskkill /im control.exe")

            # Example 133
            elif "close system restore" in text or "system restore close" in text:
                speak("Closing System Restore.")
                os.system("taskkill /im rstrui.exe")

            # Example 134
            elif "close Windows features" in text or "Windows features close" in text:
                speak("Closing Windows Features.")
                os.system("taskkill /im optionalfeatures.exe")

            # Example 135
            elif "close language preferences" in text or "language preferences close" in text:
                speak("Closing Language Preferences.")
                os.system("taskkill /im control.exe")

            # Example 136
            elif "close credential manager" in text or "credential manager close" in text:
                speak("Closing Credential Manager.")
                os.system("taskkill /im rundll32.exe")

            # Example 137
            elif "close system configuration" in text or "system configuration close" in text:
                speak("Closing System Configuration.")
                os.system("taskkill /im msconfig.exe")

            # Example 138
            elif "close system properties" in text or "system properties close" in text:
                speak("Closing System Properties.")
                os.system("taskkill /im sysdm.cpl")

            # Example 139
            elif "close task scheduler" in text or "task scheduler close" in text:
                speak("Closing Task Scheduler.")
                os.system("taskkill /im taskschd.msc")

            # Example 140
            elif "close file explorer" in text or "file explorer close" in text:
                speak("Closing File Explorer.")
                os.system("taskkill /im explorer.exe")

            # Add more examples as needed
            # Example 141
            elif "close system configuration" in text or "system configuration close" in text:
                speak("Closing System Configuration.")
                os.system("taskkill /im msconfig.exe")

            # Example 142
            elif "close firewall settings" in text or "firewall settings close" in text:
                speak("Closing Firewall Settings.")
                os.system("taskkill /im firewall.cpl")

            # Example 143
            elif "close Bluetooth settings" in text or "Bluetooth settings close" in text:
                speak("Closing Bluetooth Settings.")
                os.system("taskkill /im fsquirt.exe")

            # Example 144
            elif "close keyboard settings" in text or "keyboard settings close" in text:
                speak("Closing Keyboard Settings.")
                os.system("taskkill /im control.exe")

            # Example 145
            elif "close mouse settings" in text or "mouse settings close" in text:
                speak("Closing Mouse Settings.")
                os.system("taskkill /im control.exe")

            # Example 146
            elif "close date and time settings" in text or "date and time close" in text:
                speak("Closing Date and Time Settings.")
                os.system("taskkill /im timedate.cpl")

            # Example 147
            elif "close task manager" in text or "task manager close" in text:
                speak("Closing Task Manager.")
                os.system("taskkill /im taskmgr.exe")

            # Example 148
            elif "close system monitor" in text or "system monitor close" in text:
                speak("Closing System Monitor.")
                os.system("taskkill /im perfmon.exe")

            # Example 149
            elif "close device manager" in text or "device manager close" in text:
                speak("Closing Device Manager.")
                os.system("taskkill /im devmgmt.msc")

            # Example 150
            elif "close power options" in text or "power options close" in text:
                speak("Closing Power Options.")
                os.system("taskkill /im powercfg.cpl")

            # Add more examples as needed
            # Example 151
            elif "close sound settings" in text or "sound settings close" in text:
                speak("Closing Sound Settings.")
                os.system("taskkill /im mmsys.cpl")

            # Example 152
            elif "close privacy settings" in text or "privacy settings close" in text:
                speak("Closing Privacy Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 153
            elif "close storage settings" in text or "storage settings close" in text:
                speak("Closing Storage Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 154
            elif "close update history" in text or "update history close" in text:
                speak("Closing Update History.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 155
            elif "close reliability monitor" in text or "reliability monitor close" in text:
                speak("Closing Reliability Monitor.")
                os.system("taskkill /im perfmon.exe")

            # Example 156
            elif "close performance settings" in text or "performance settings close" in text:
                speak("Closing Performance Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 157
            elif "close language preferences" in text or "language preferences close" in text:
                speak("Closing Language Preferences.")
                os.system("taskkill /im control.exe")

            # Example 158
            elif "close system security" in text or "system security close" in text:
                speak("Closing System Security.")
                os.system("taskkill /im WindowsSecurity.exe")

            # Example 159
            elif "close remote desktop" in text or "remote desktop close" in text:
                speak("Closing Remote Desktop.")
                os.system("taskkill /im mstsc.exe")

            # Example 160
            elif "close control firewall" in text or "firewall close" in text:
                speak("Closing Firewall Settings.")
                os.system("taskkill /im firewall.cpl")

            # Example 161
            elif "close system monitor" in text or "system monitor close" in text:
                speak("Closing System Monitor.")
                os.system("taskkill /im perfmon.exe")

            # Example 162
            elif "close device installation settings" in text or "device installation close" in text:
                speak("Closing Device Installation Settings.")
                os.system("taskkill /im ms-settings:windowsupdate-deviceoptions")

            # Example 163
            elif "close system screen settings" in text or "screen settings close" in text:
                speak("Closing Screen Settings.")
                os.system("taskkill /im ms-settings:display")

            # Example 164
            elif "close system power plan" in text or "power plan close" in text:
                speak("Closing Power Plan Settings.")
                os.system("taskkill /im powercfg.cpl")

            # Example 165
            elif "close system user accounts" in text or "user accounts close" in text:
                speak("Closing User Accounts.")
                os.system("taskkill /im netplwiz.exe")

            # Example 166
            elif "close system sound settings" in text or "sound settings close" in text:
                speak("Closing Sound Settings.")
                os.system("taskkill /im mmsys.cpl")

            # Example 167
            elif "close system privacy dashboard" in text or "privacy dashboard close" in text:
                speak("Closing Privacy Dashboard.")
                os.system("taskkill /im ms-settings:privacy-feedback")

            # Example 168
            elif "close system screen saver settings" in text or "screen saver settings close" in text:
                speak("Closing Screen Saver Settings.")
                os.system("taskkill /im control.exe")

            # Example 169
            elif "close system network adapters" in text or "network adapters close" in text:
                speak("Closing Network Adapters.")
                os.system("taskkill /im ncpa.cpl")

            # Example 170
            elif "close system game mode settings" in text or "game mode settings close" in text:
                speak("Closing Game Mode Settings.")
                os.system("taskkill /im ms-settings:gaming-gamemode")

            # Example 171
            elif "close system privacy diagnostics" in text or "privacy diagnostics close" in text:
                speak("Closing Privacy Diagnostics.")
                os.system("taskkill /im ms-settings:privacy-diagnostics")

            # Example 172
            elif "close system region and language settings" in text or "region and language close" in text:
                speak("Closing Region and Language Settings.")
                os.system("taskkill /im control.exe")

            # Example 173
            elif "close system display color calibration" in text or "display color calibration close" in text:
                speak("Closing Display Color Calibration.")
                os.system("taskkill /im dccw.exe")

            # Example 174
            elif "close system recovery" in text or "system recovery close" in text:
                speak("Closing System Recovery.")
                os.system("taskkill /im control.exe")

            # Example 175
            elif "close system DirectX diagnostic tool" in text or "DirectX diagnostic tool close" in text:
                speak("Closing DirectX Diagnostic Tool.")
                os.system("taskkill /im dxdiag.exe")

            # Add more examples as needed
            # Example 176
            elif "close taskbar settings" in text or "taskbar settings close" in text:
                speak("Closing Taskbar Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 177
            elif "close Windows update history" in text or "update history close" in text:
                speak("Closing Windows Update History.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 178
            elif "close system reliability monitor" in text or "reliability monitor close" in text:
                speak("Closing System Reliability Monitor.")
                os.system("taskkill /im perfmon.exe")

            # Example 179
            elif "close system performance settings" in text or "performance settings close" in text:
                speak("Closing Performance Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 180
            elif "close system privacy settings" in text or "privacy settings close" in text:
                speak("Closing Privacy Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 181
            elif "close system storage settings" in text or "storage settings close" in text:
                speak("Closing Storage Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 182
            elif "close system update check" in text or "update check close" in text:
                speak("Closing Update Check.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 183
            elif "close system screen settings" in text or "screen settings close" in text:
                speak("Closing Screen Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 184
            elif "close system power plan" in text or "power plan close" in text:
                speak("Closing Power Plan Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 185
            elif "close system user accounts" in text or "user accounts close" in text:
                speak("Closing User Accounts.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 186
            elif "close program and features" in text or "programs and features close" in text:
                speak("Closing Programs and Features.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 187
            elif "close device and printers" in text or "devices and printers close" in text:
                speak("Closing Devices and Printers.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 188
            elif "close system restore" in text or "system restore close" in text:
                speak("Closing System Restore.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 189
            elif "close Windows security" in text or "Windows security close" in text:
                speak("Closing Windows Security.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 190
            elif "close remote desktop" in text or "remote desktop close" in text:
                speak("Closing Remote Desktop.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 191
            elif "close control panel" in text or "control panel close" in text:
                speak("Closing Control Panel.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 192
            elif "close device manager" in text or "device manager close" in text:
                speak("Closing Device Manager.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 193
            elif "close power options" in text or "power options close" in text:
                speak("Closing Power Options.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 194
            elif "close sound settings" in text or "sound settings close" in text:
                speak("Closing Sound Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 195
            elif "close system security" in text or "system security close" in text:
                speak("Closing System Security.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 196
            elif "close remote desktop" in text or "remote desktop close" in text:
                speak("Closing Remote Desktop.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 197
            elif "close control firewall" in text or "firewall close" in text:
                speak("Closing Firewall Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 198
            elif "close system monitor" in text or "system monitor close" in text:
                speak("Closing System Monitor.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 199
            elif "close device installation settings" in text or "device installation close" in text:
                speak("Closing Device Installation Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Example 200
            elif "close system screen settings" in text or "screen settings close" in text:
                speak("Closing Screen Settings.")
                os.system("taskkill /im SystemSettings.exe")

            # Add more examples as needed
            # 1
            elif "go to address bar" in text or "address bar" in text:
                speak("Going to Address Bar.")
                gui.hotkey("alt", "d")

            # 2
            elif "zoom in" in text:
                speak("Zooming In.")
                gui.hotkey("ctrl", "+")

            # 3
            elif "zoom out" in text:
                speak("Zooming Out.")
                gui.hotkey("ctrl", "-")

            # 4
            elif "reset zoom" in text or "default zoom" in text:
                speak("Resetting Zoom.")
                gui.hotkey("ctrl", "0")

            # 5
            elif "search" in text or "search bar" in text:
                speak("Activating Search Bar.")
                gui.hotkey("ctrl", "k")

            # 6
            elif "new window" in text or "open new window" in text:
                speak("Opening New Window.")
                gui.hotkey("ctrl", "n")

            # 7
            elif "close window" in text:
                speak("Closing Window.")
                gui.hotkey("alt", "f4")

            # 8
            elif "minimize window" in text:
                speak("Minimizing Window.")
                gui.hotkey("win", "down")

            # 9
            elif "maximize window" in text:
                speak("Maximizing Window.")
                gui.hotkey("win", "up")

            # 10
            elif "restore window" in text:
                speak("Restoring Window.")
                gui.hotkey("win", "shift", "up")

            # 11
            elif "switch window" in text or "next window" in text:
                speak("Switching to Next Window.")
                gui.hotkey("alt", "tab")

            # 12
            elif "previous window" in text or "back window" in text:
                speak("Switching to Previous Window.")
                gui.hotkey("alt", "shift", "tab")

            # 13
            elif "open incognito" in text or "private window" in text:
                speak("Opening Incognito Window.")
                gui.hotkey("ctrl", "shift", "n")

            # 14
            elif "bookmark page" in text or "save page" in text:
                speak("Bookmarking Page.")
                gui.hotkey("ctrl", "d")

            # 15
            elif "history" in text or "browse history" in text:
                speak("Opening Browsing History.")
                gui.hotkey("ctrl", "h")

            # 16
            elif "downloads" in text or "download history" in text:
                speak("Opening Downloads History.")
                gui.hotkey("ctrl", "j")

            # 17
            elif "inspect element" in text or "open developer tools" in text:
                speak("Opening Developer Tools.")
                gui.hotkey("ctrl", "shift", "i")

            # 18
            elif "clear cookies" in text or "delete cookies" in text:
                speak("Clearing Cookies.")
                gui.hotkey("ctrl", "shift", "del")

            # 19
            elif "fullscreen" in text or "full screen" in text:
                speak("Entering Fullscreen Mode.")
                gui.hotkey("f11")

            # 20
            elif "toggle dark mode" in text or "dark theme" in text:
                speak("Toggling Dark Mode.")
                gui.hotkey("ctrl", "shift", "e")

            # 21
            elif "mute" in text or "mute tab" in text:
                speak("Muting Tab.")
                gui.hotkey("ctrl", "m")

            # 22
            elif "unmute" in text or "unmute tab" in text:
                speak("Unmuting Tab.")
                gui.hotkey("ctrl", "shift", "m")

            # 23
            elif "open extensions" in text or "manage extensions" in text:
                speak("Opening Extensions.")
                gui.hotkey("ctrl", "shift", "a")

            # 24
            elif "open settings" in text or "browser settings" in text:
                speak("Opening Settings.")
                gui.hotkey("ctrl", ",")

            # 25
            elif "save page as" in text or "save as" in text:
                speak("Saving Page As.")
                gui.hotkey("ctrl", "s")

            # 26
            elif "print page" in text or "print" in text:
                speak("Printing Page.")
                gui.hotkey("ctrl", "p")
            # 26
            elif "open history" in text or "view history" in text:
                speak("Opening History.")
                gui.hotkey("ctrl", "h")

            # 27
            elif "clear browsing data" in text or "clear history" in text:
                speak("Clearing Browsing Data.")
                gui.hotkey("ctrl", "shift", "del")

            # 28
            elif "open bookmarks" in text or "view bookmarks" in text:
                speak("Opening Bookmarks.")
                gui.hotkey("ctrl", "b")

            # 29
            elif "open downloads" in text or "view downloads" in text:
                speak("Opening Downloads.")
                gui.hotkey("ctrl", "j")

            # 30
            elif "open settings" in text or "browser settings" in text:
                speak("Opening Settings.")
                gui.hotkey("ctrl", ",")

            # 31
            elif "save page as" in text or "save as" in text:
                speak("Saving Page As.")
                gui.hotkey("ctrl", "s")

            # 32
            elif "print page" in text or "print" in text:
                speak("Printing Page.")
                gui.hotkey("ctrl", "p")

            # 33
            elif "open incognito" in text or "private window" in text:
                speak("Opening Incognito Window.")
                gui.hotkey("ctrl", "shift", "n")

            # 34
            elif "toggle dark mode" in text or "dark theme" in text:
                speak("Toggling Dark Mode.")
                gui.hotkey("ctrl", "shift", "e")

            # 35
            elif "mute" in text or "mute tab" in text:
                speak("Muting Tab.")
                gui.hotkey("ctrl", "m")

            # 36
            elif "unmute" in text or "unmute tab" in text:
                speak("Unmuting Tab.")
                gui.hotkey("ctrl", "shift", "m")

            # 37
            elif "open extensions" in text or "manage extensions" in text:
                speak("Opening Extensions.")
                gui.hotkey("ctrl", "shift", "a")

            # 38
            elif "inspect element" in text or "open developer tools" in text:
                speak("Opening Developer Tools.")
                gui.hotkey("ctrl", "shift", "i")

            # 39
            elif "open task manager" in text or "browser task manager" in text:
                speak("Opening Task Manager.")
                gui.hotkey("shift", "esc")

            # 40
            elif "reload page" in text or "refresh" in text:
                speak("Reloading Page.")
                gui.hotkey("ctrl", "r")

            # 41
            elif "go back" in text or "back" in text:
                speak("Going Back.")
                gui.hotkey("alt", "left")

            # 42
            elif "go forward" in text or "forward" in text:
                speak("Going Forward.")
                gui.hotkey("alt", "right")

            # 43
            elif "stop loading" in text or "stop" in text:
                speak("Stopping Page Load.")
                gui.hotkey("esc")

            # 44
            elif "scroll up" in text or "scroll page up" in text:
                speak("Scrolling Up.")
                pyautogui.scroll(3)

            # 45
            elif "scroll down" in text or "scroll page down" in text:
                speak("Scrolling Down.")
                pyautogui.scroll(-3)

            # 46
            elif "scroll to top" in text:
                speak("Scrolling to Top.")
                pyautogui.press("home")

            # 47
            elif "scroll to bottom" in text:
                speak("Scrolling to Bottom.")
                pyautogui.press("end")

            # 48
            elif "open new tab" in text or "new tab" in text:
                speak("Opening New Tab.")
                gui.hotkey("ctrl", "t")

            # 49


            # 50
            elif "reopen closed tab" in text or "restore closed tab" in text:
                speak("Reopening Closed Tab.")
                gui.hotkey("ctrl", "shift", "t")

            # 51
            elif "switch to tab" in text or "go to tab" in text:
                speak("Switching to Tab.")
                gui.hotkey("ctrl", "1")  # Change the number for different tabs

            # 52
            elif "open link in new tab" in text or "open link in background" in text:
                speak("Opening Link in New Tab.")
                gui.hotkey("ctrl", "click")

            # 53
            elif "duplicate tab" in text or "clone tab" in text:
                speak("Duplicating Tab.")
                gui.hotkey("ctrl", "shift", "d")

            # 54
            elif "bookmark current page" in text or "add bookmark" in text:
                speak("Bookmarking Current Page.")
                gui.hotkey("ctrl", "d")

            # 55
            elif "history" in text or "view history" in text:
                speak("Viewing Browsing History.")
                gui.hotkey("ctrl", "h")

            # 56
            elif "restore closed window" in text or "reopen closed window" in text:
                speak("Restoring Closed Window.")
                gui.hotkey("ctrl", "shift", "n")

            # 57
            elif "open private window" in text or "open incognito window" in text:
                speak("Opening Private Window.")
                gui.hotkey("ctrl", "shift", "n")

            # 58
            elif "minimize all windows" in text or "show desktop" in text:
                speak("Minimizing All Windows.")
                gui.hotkey("win", "d")

            # 59
            elif "show desktop" in text or "hide windows" in text:
                speak("Showing Desktop.")
                gui.hotkey("win", "m")

            # 60
            elif "open task view" in text or "view tasks" in text:
                speak("Opening Task View.")
                gui.hotkey("win", "tab")

            # 61
            elif "switch virtual desktop" in text or "change desktop" in text:
                speak("Switching Virtual Desktop.")
                gui.hotkey("ctrl", "win", "right")

            # 62
            elif "open notification center" in text or "show notifications" in text:
                speak("Opening Notification Center.")
                gui.hotkey("win", "a")

            # 63
            elif "show action center" in text or "show action menu" in text:
                speak("Showing Action Center.")
                gui.hotkey("win", "a")

            # 64
            elif "lock screen" in text or "lock computer" in text:
                speak("Locking Screen.")
                gui.hotkey("win", "l")

            # 65
            elif "switch user" in text or "change user" in text:
                speak("Switching User.")
                gui.hotkey("win", "l")

            # 66
            elif "log off" in text or "sign out" in text:
                speak("Logging Off.")
                gui.hotkey("ctrl", "alt", "del")

            # 67
            elif "shutdown" in text or "turn off computer" in text:
                speak("Shutting Down.")
                gui.hotkey("alt", "f4")

            # 68
            elif "restart" in text or "reboot" in text:
                speak("Restarting.")
                gui.hotkey("ctrl", "alt", "del")

            # 69
            elif "sleep" in text or "put computer to sleep" in text:
                speak("Putting Computer to Sleep.")
                gui.hotkey("alt", "f4")

            # 70
            elif "hibernate" in text or "enable hibernation" in text:
                speak("Hibernating.")
                gui.hotkey("alt", "f4")

            # 71
            elif "open file explorer" in text or "file explorer" in text:
                speak("Opening File Explorer.")
                gui.hotkey("win", "e")

            # 72
            elif "open control panel" in text or "control panel" in text:
                speak("Opening Control Panel.")
                gui.hotkey("win", "r")
                gui.write("control")
                gui.press("enter")

            # 73
            elif "open task manager" in text or "task manager" in text:
                speak("Opening Task Manager.")
                gui.hotkey("ctrl", "shift", "esc")

            # 74
            elif "open command prompt" in text or "command prompt" in text:
                speak("Opening Command Prompt.")
                gui.hotkey("win", "r")
                gui.write("cmd")
                gui.press("enter")

            # 75
            elif "open PowerShell" in text or "PowerShell" in text:
                speak("Opening PowerShell.")
                gui.hotkey("win", "x")
                gui.write("powershell")
                gui.press("enter")
            # 76
            elif "open task scheduler" in text or "task scheduler" in text:
                speak("Opening Task Scheduler.")
                gui.hotkey("win", "r")
                gui.write("taskschd.msc")
                gui.press("enter")

            # 77
            elif "open registry editor" in text or "registry editor" in text:
                speak("Opening Registry Editor.")
                gui.hotkey("win", "r")
                gui.write("regedit")
                gui.press("enter")

            # 78
            elif "open device manager" in text or "device manager" in text:
                speak("Opening Device Manager.")
                gui.hotkey("win", "x")
                gui.write("devmgmt.msc")
                gui.press("enter")

            # 79
            elif "open system properties" in text or "system properties" in text:
                speak("Opening System Properties.")
                gui.hotkey("win", "pause")

            # 80
            elif "open system information" in text or "system information" in text:
                speak("Opening System Information.")
                gui.hotkey("win", "r")
                gui.write("msinfo32")
                gui.press("enter")

            # 81
            elif "open disk management" in text or "disk management" in text:
                speak("Opening Disk Management.")
                gui.hotkey("win", "x")
                gui.write("diskmgmt.msc")
                gui.press("enter")

            # 82
            elif "open network connections" in text or "network connections" in text:
                speak("Opening Network Connections.")
                gui.hotkey("win", "r")
                gui.write("ncpa.cpl")
                gui.press("enter")

            # 83
            elif "open power options" in text or "power options" in text:
                speak("Opening Power Options.")
                gui.hotkey("win", "x")
                gui.write("powercfg.cpl")
                gui.press("enter")

            # 84
            elif "open sound settings" in text or "sound settings" in text:
                speak("Opening Sound Settings.")
                gui.hotkey("win", "r")
                gui.write("mmsys.cpl")
                gui.press("enter")

            # 85
            elif "open display settings" in text or "display settings" in text:
                speak("Opening Display Settings.")
                gui.hotkey("win", "i")
                gui.write("display")
                gui.press("enter")

            # 86
            elif "open system configuration" in text or "system configuration" in text:
                speak("Opening System Configuration.")
                gui.hotkey("win", "r")
                gui.write("msconfig")
                gui.press("enter")

            # 87
            elif "open remote desktop" in text or "remote desktop" in text:
                speak("Opening Remote Desktop.")
                gui.hotkey("win", "s")
                gui.write("Remote Desktop Connection")
                gui.press("enter")

            # 88
            elif "open credential manager" in text or "credential manager" in text:
                speak("Opening Credential Manager.")
                gui.hotkey("win", "s")
                gui.write("Credential Manager")
                gui.press("enter")

            # 89
            elif "open programs and features" in text or "programs and features" in text:
                speak("Opening Programs and Features.")
                gui.hotkey("win", "r")
                gui.write("appwiz.cpl")
                gui.press("enter")

            # 90
            elif "open Windows security" in text or "Windows security" in text:
                speak("Opening Windows Security.")
                gui.hotkey("win", "i")
                gui.write("Windows Security")
                gui.press("enter")

            # 91
            elif "open Windows update settings" in text or "Windows update settings" in text:
                speak("Opening Windows Update Settings.")
                gui.hotkey("win", "i")
                gui.write("Windows Update")
                gui.press("enter")

            # 92
            elif "open system environment variables" in text or "system environment variables" in text:
                speak("Opening System Environment Variables.")
                gui.hotkey("win", "s")
                gui.write("Environment Variables")
                gui.press("enter")

            # 93
            elif "open advanced system settings" in text or "advanced system settings" in text:
                speak("Opening Advanced System Settings.")
                gui.hotkey("win", "s")
                gui.write("Advanced System Settings")
                gui.press("enter")

            # 94
            elif "open file history settings" in text or "file history settings" in text:
                speak("Opening File History Settings.")
                gui.hotkey("win", "s")
                gui.write("File History Settings")
                gui.press("enter")

            # 95
            elif "open recovery settings" in text or "recovery settings" in text:
                speak("Opening Recovery Settings.")
                gui.hotkey("win", "s")
                gui.write("Recovery Settings")
                gui.press("enter")

            # 96
            elif "open ease of access center" in text or "ease of access center" in text:
                speak("Opening Ease of Access Center.")
                gui.hotkey("win", "s")
                gui.write("Ease of Access Center")
                gui.press("enter")

            # 97
            elif "open network and sharing center" in text or "network and sharing center" in text:
                speak("Opening Network and Sharing Center.")
                gui.hotkey("win", "s")
                gui.write("Network and Sharing Center")
                gui.press("enter")

            # 98
            elif "open system backup and restore" in text or "system backup and restore" in text:
                speak("Opening System Backup and Restore.")
                gui.hotkey("win", "s")
                gui.write("Backup and Restore (Windows 7)")
                gui.press("enter")

            # 99
            elif "open region and language settings" in text or "region and language settings" in text:
                speak("Opening Region and Language Settings.")
                gui.hotkey("win", "s")
                gui.write("Region and Language")
                gui.press("enter")

            # 100
            elif "open user accounts" in text or "user accounts" in text:
                speak("Opening User Accounts.")
                gui.hotkey("win", "s")
                gui.write("User Accounts")
                gui.press("enter")
            # Open Commands
            # 1
            elif "open task scheduler" in text or "task scheduler" in text:
                speak("Opening Task Scheduler.")
                gui.hotkey("win", "r")
                gui.write("taskschd.msc")
                gui.press("enter")

            # 2
            elif "open registry editor" in text or "registry editor" in text:
                speak("Opening Registry Editor.")
                gui.hotkey("win", "r")
                gui.write("regedit")
                gui.press("enter")

            # 3
            elif "open device manager" in text or "device manager" in text:
                speak("Opening Device Manager.")
                gui.hotkey("win", "x")
                gui.write("devmgmt.msc")
                gui.press("enter")

            # 4
            elif "open system properties" in text or "system properties" in text:
                speak("Opening System Properties.")
                gui.hotkey("win", "pause")

            # 5
            elif "open system information" in text or "system information" in text:
                speak("Opening System Information.")
                gui.hotkey("win", "r")
                gui.write("msinfo32")
                gui.press("enter")

            # 6
            elif "open disk management" in text or "disk management" in text:
                speak("Opening Disk Management.")
                gui.hotkey("win", "x")
                gui.write("diskmgmt.msc")
                gui.press("enter")

            # 7
            elif "open network connections" in text or "network connections" in text:
                speak("Opening Network Connections.")
                gui.hotkey("win", "r")
                gui.write("ncpa.cpl")
                gui.press("enter")

            # 8
            elif "open power options" in text or "power options" in text:
                speak("Opening Power Options.")
                gui.hotkey("win", "x")
                gui.write("powercfg.cpl")
                gui.press("enter")

            # 9
            elif "open sound settings" in text or "sound settings" in text:
                speak("Opening Sound Settings.")
                gui.hotkey("win", "r")
                gui.write("mmsys.cpl")
                gui.press("enter")

            # 10
            elif "open display settings" in text or "display settings" in text:
                speak("Opening Display Settings.")
                gui.hotkey("win", "i")
                gui.write("display")
                gui.press("enter")

            # 11
            elif "open system configuration" in text or "system configuration" in text:
                speak("Opening System Configuration.")
                gui.hotkey("win", "r")
                gui.write("msconfig")
                gui.press("enter")

            # 12
            elif "open remote desktop" in text or "remote desktop" in text:
                speak("Opening Remote Desktop.")
                gui.hotkey("win", "s")
                gui.write("Remote Desktop Connection")
                gui.press("enter")

            # 13
            elif "open credential manager" in text or "credential manager" in text:
                speak("Opening Credential Manager.")
                gui.hotkey("win", "s")
                gui.write("Credential Manager")
                gui.press("enter")

            # 14
            elif "open programs and features" in text or "programs and features" in text:
                speak("Opening Programs and Features.")
                gui.hotkey("win", "r")
                gui.write("appwiz.cpl")
                gui.press("enter")

            # 15
            elif "open Windows security" in text or "Windows security" in text:
                speak("Opening Windows Security.")
                gui.hotkey("win", "i")
                gui.write("Windows Security")
                gui.press("enter")

            # 16
            elif "open Windows update settings" in text or "Windows update settings" in text:
                speak("Opening Windows Update Settings.")
                gui.hotkey("win", "i")
                gui.write("Windows Update")
                gui.press("enter")

            # 17
            elif "open system environment variables" in text or "system environment variables" in text:
                speak("Opening System Environment Variables.")
                gui.hotkey("win", "s")
                gui.write("Environment Variables")
                gui.press("enter")

            # 18
            elif "open advanced system settings" in text or "advanced system settings" in text:
                speak("Opening Advanced System Settings.")
                gui.hotkey("win", "s")
                gui.write("Advanced System Settings")
                gui.press("enter")

            # 19
            elif "open file history settings" in text or "file history settings" in text:
                speak("Opening File History Settings.")
                gui.hotkey("win", "s")
                gui.write("File History Settings")
                gui.press("enter")

            # 20
            elif "open recovery settings" in text or "recovery settings" in text:
                speak("Opening Recovery Settings.")
                gui.hotkey("win", "s")
                gui.write("Recovery Settings")
                gui.press("enter")

            # 21
            elif "open ease of access center" in text or "ease of access center" in text:
                speak("Opening Ease of Access Center.")
                gui.hotkey("win", "s")
                gui.write("Ease of Access Center")
                gui.press("enter")

            # 22
            elif "open network and sharing center" in text or "network and sharing center" in text:
                speak("Opening Network and Sharing Center.")
                gui.hotkey("win", "s")
                gui.write("Network and Sharing Center")
                gui.press("enter")

            # 23
            elif "open system backup and restore" in text or "system backup and restore" in text:
                speak("Opening System Backup and Restore.")
                gui.hotkey("win", "s")
                gui.write("Backup and Restore (Windows 7)")
                gui.press("enter")

            # 24
            elif "open region and language settings" in text or "region and language settings" in text:
                speak("Opening Region and Language Settings.")
                gui.hotkey("win", "s")
                gui.write("Region and Language")
                gui.press("enter")

            # 25
            elif "open user accounts" in text or "user accounts" in text:
                speak("Opening User Accounts.")
                gui.hotkey("win", "s")
                gui.write("User Accounts")
                gui.press("enter")


            # Close Commands
            # 26
            elif "close task scheduler" in text or "close the task scheduler" in text:
                speak("Closing Task Scheduler.")
                gui.hotkey("alt", "f4")

            # 27
            elif "close registry editor" in text or "close the registry editor" in text:
                speak("Closing Registry Editor.")
                gui.hotkey("alt", "f4")

            # 28
            elif "close device manager" in text or "close the device manager" in text:
                speak("Closing Device Manager.")
                gui.hotkey("alt", "f4")

            # 29
            elif "close system properties" in text or "close the system properties" in text:
                speak("Closing System Properties.")
                gui.hotkey("alt", "f4")

            # 30
            elif "close system information" in text or "close the system information" in text:
                speak("Closing System Information.")
                gui.hotkey("alt", "f4")

            # 31
            elif "close disk management" in text or "close the disk management" in text:
                speak("Closing Disk Management.")
                gui.hotkey("alt", "f4")

            # 32
            elif "close network connections" in text or "close the network connections" in text:
                speak("Closing Network Connections.")
                gui.hotkey("alt", "f4")

            # 33
            elif "close power options" in text or "close the power options" in text:
                speak("Closing Power Options.")
                gui.hotkey("alt", "f4")

            # 34
            elif "close sound settings" in text or "close the sound settings" in text:
                speak("Closing Sound Settings.")
                gui.hotkey("alt", "f4")

            # 35
            elif "close display settings" in text or "close the display settings" in text:
                speak("Closing Display Settings.")
                gui.hotkey("alt", "f4")

            # 36
            elif "close system configuration" in text or "close the system configuration" in text:
                speak("Closing System Configuration.")
                gui.hotkey("alt", "f4")

            # 37
            elif "close remote desktop" in text or "close the remote desktop" in text:
                speak("Closing Remote Desktop.")
                gui.hotkey("alt", "f4")

            # 38
            elif "close credential manager" in text or "close the credential manager" in text:
                speak("Closing Credential Manager.")
                gui.hotkey("alt", "f4")

            # 39
            elif "close programs and features" in text or "close the programs and features" in text:
                speak("Closing Programs and Features.")
                gui.hotkey("alt", "f4")

            # 40
            elif "close Windows security" in text or "close the Windows security" in text:
                speak("Closing Windows Security.")
                gui.hotkey("alt", "f4")

            # 41
            elif "close Windows update settings" in text or "close the Windows update settings" in text:
                speak("Closing Windows Update Settings.")
                gui.hotkey("alt", "f4")

            # 42
            elif "close system environment variables" in text or "close the system environment variables" in text:
                speak("Closing System Environment Variables.")
                gui.hotkey("alt", "f4")

            # 43
            elif "close advanced system settings" in text or "close the advanced system settings" in text:
                speak("Closing Advanced System Settings.")
                gui.hotkey("alt", "f4")

            # 44
            elif "close file history settings" in text or "close the file history settings" in text:
                speak("Closing File History Settings.")
                gui.hotkey("alt", "f4")

            # 45
            elif "close recovery settings" in text or "close the recovery settings" in text:
                speak("Closing Recovery Settings.")
                gui.hotkey("alt", "f4")

            # 46
            elif "close ease of access center" in text or "close the ease of access center" in text:
                speak("Closing Ease of Access Center.")
                gui.hotkey("alt", "f4")

            # 47
            elif "close network and sharing center" in text or "close the network and sharing center" in text:
                speak("Closing Network and Sharing Center.")
                gui.hotkey("alt", "f4")

            # 48
            elif "close system backup and restore" in text or "close the system backup and restore" in text:
                speak("Closing System Backup and Restore.")
                gui.hotkey("alt", "f4")

            # 49
            elif "close region and language settings" in text or "close the region and language settings" in text:
                speak("Closing Region and Language Settings.")
                gui.hotkey("alt", "f4")

            # 50
            elif "close user accounts" in text or "close the user accounts" in text:
                speak("Closing User Accounts.")
                gui.hotkey("alt", "f4")

            # 1
            elif "move mouse" in text or "move cursor" in text:
                speak("Moving the mouse to the center of the screen.")
                gui.moveTo(gui.size()[0] / 2, gui.size()[1] / 2)

            # 2
            elif "double click" in text or "perform double click" in text:
                speak("Performing a double-click.")
                gui.doubleClick()

            # 3
            elif "right click" in text or "perform right click" in text:
                speak("Performing a right-click.")
                gui.rightClick()

            # 4
            elif "scroll down" in text or "scroll the page down" in text:
                speak("Scrolling the page down.")
                gui.scroll(-1)

            # 5
            elif "type message" in text or "type text" in text:
                speak("Typing a sample message.")
                gui.typewrite("Hello, PyAutoGUI!")

            # 6
            elif "press enter" in text or "hit enter key" in text:
                speak("Pressing the Enter key.")
                gui.press("enter")

            # 7
            elif "press space" in text or "hit spacebar" in text:
                speak("Pressing the Spacebar.")
                gui.press("space")

            # 8
            elif "press tab" in text or "hit tab key" in text:
                speak("Pressing the Tab key.")
                gui.press("tab")

            # 9
            elif "press esc" in text or "hit escape key" in text:
                speak("Pressing the Escape key.")
                gui.press("esc")

            # 10
            elif "take screenshot" in text or "capture screen" in text:
                speak("Taking a screenshot.")
                gui.screenshot("screenshot.png")

            # 11
            elif "find image" in text or "locate image" in text:
                speak("Finding the coordinates of a sample image.")
                coordinates = gui.locateOnScreen("sample_image.png")
                print("Image found at:", coordinates)

            # 12
            elif "toggle caps lock" in text or "caps lock on" in text:
                speak("Toggling Caps Lock.")
                gui.press("capslock")

            # 13
            elif "hold key" in text or "keep key pressed" in text:
                speak("Holding the 'A' key.")
                gui.keyDown("a")

            # 14
            elif "release key" in text or "let go of key" in text:
                speak("Releasing the 'A' key.")
                gui.keyUp("a")

            # 15
            elif "change mouse speed" in text or "adjust mouse sensitivity" in text:
                speak("Setting the mouse speed to 2x.")
                gui.mouseInfo = (2, gui.mouseInfo[1])

            # 16
            elif "open calculator" in text or "launch calculator" in text:
                speak("Opening the Calculator.")
                gui.hotkey("win", "r")
                gui.typewrite("calc")
                gui.press("enter")

            # 17
            elif "copy text" in text or "copy to clipboard" in text:
                speak("Copying the sample text to the clipboard.")
                gui.typewrite("Copy this text to clipboard.")
                gui.hotkey("ctrl", "c")

            # 18
            elif "paste text" in text or "paste from clipboard" in text:
                speak("Pasting text from the clipboard.")
                gui.hotkey("ctrl", "v")

            # 19
            elif "undo" in text or "undo action" in text:
                speak("Undoing the last action.")
                gui.hotkey("ctrl", "z")

            # 20
            elif "redo" in text or "redo action" in text:
                speak("Redoing the last undone action.")
                gui.hotkey("ctrl", "y")

            # 21
            elif "cut text" in text or "cut to clipboard" in text:
                speak("Cutting the sample text to clipboard.")
                gui.hotkey("ctrl", "x")

            # 22
            elif "select all" in text or "select entire document" in text:
                speak("Selecting all text in the document.")
                gui.hotkey("ctrl", "a")

            # 23
            elif "save file" in text or "save current document" in text:
                speak("Saving the current document.")
                gui.hotkey("ctrl", "s")

            # 24
            elif "print document" in text or "print current page" in text:
                speak("Printing the current document.")
                gui.hotkey("ctrl", "p")

            # 25
            elif "find text" in text or "search for text" in text:
                speak("Opening the find dialog to search for text.")
                gui.hotkey("ctrl", "f")

            # 26
            elif "open new tab" in text or "launch new browser tab" in text:
                speak("Opening a new browser tab.")
                gui.hotkey("ctrl", "t")

            # 28
            elif "switch tab" in text or "move to next tab" in text:
                speak("Switching to the next browser tab.")
                gui.hotkey("ctrl", "tab")

            # 29
            elif "go back" in text or "navigate back" in text:
                speak("Navigating back to the previous page.")
                gui.hotkey("alt", "left")

            # 30
            elif "go forward" in text or "navigate forward" in text:
                speak("Navigating forward to the next page.")
                gui.hotkey("alt", "right")

            # 31
            elif "zoom in" in text or "increase zoom" in text:
                speak("Zooming in on the current page.")
                gui.hotkey("ctrl", "+")

            # 32
            elif "zoom out" in text or "decrease zoom" in text:
                speak("Zooming out on the current page.")
                gui.hotkey("ctrl", "-")

            # 33
            elif "reset zoom" in text or "restore default zoom" in text:
                speak("Resetting the zoom level to default.")
                gui.hotkey("ctrl", "0")

            # 34
            elif "open settings" in text or "launch settings" in text:
                speak("Opening the application settings.")
                gui.hotkey("ctrl", ",")

            # 35
            elif "toggle full screen" in text or "enter full screen mode" in text:
                speak("Toggling Fullscreen Mode.")
                gui.hotkey("f11")

            # 36
            elif "toggle dark mode" in text or "dark theme" in text:
                speak("Toggling Dark Mode.")
                gui.hotkey("ctrl", "shift", "e")

            # 37
            elif "mute" in text or "mute tab" in text:
                speak("Muting Tab.")
                gui.hotkey("ctrl", "m")

            # 38
            elif "take screenshot region" in text or "capture specific area" in text:
                speak("Taking a screenshot of a specific region.")
                region = (100, 100, 300, 300)  # Example region coordinates (left, top, width, height)
                gui.screenshot("region_screenshot.png", region=region)

            # 39
            elif "click at coordinates" in text or "perform click at position" in text:
                speak("Performing a click at specific coordinates.")
                gui.click(200, 200)

            # 40
            elif "right click at coordinates" in text or "perform right click at position" in text:
                speak("Performing a right-click at specific coordinates.")
                gui.rightClick(200, 200)

            # 41
            elif "double click at coordinates" in text or "perform double click at position" in text:
                speak("Performing a double-click at specific coordinates.")
                gui.doubleClick(200, 200)

            # 42
            elif "move mouse relative" in text or "move cursor by offset" in text:
                speak("Moving the mouse relative to its current position.")
                gui.move(50, 50, duration=1)

            # 43
            elif "scroll up" in text or "scroll the page up" in text:
                speak("Scrolling the page up.")
                gui.scroll(1)

            # 44
            elif "press key" in text or "simulate key press" in text:
                speak("Simulating pressing the 'A' key.")
                gui.press("a")

            # 45
            elif "press key sequence" in text or "simulate key sequence" in text:
                speak("Simulating pressing the key sequence 'Ctrl+A'.")
                gui.hotkey("ctrl", "a")

            # 46
            elif "type special characters" in text or "type symbols" in text:
                speak("Typing special characters: @#$%^&*()")
                gui.typewrite("@#$%^&*()")

            # 47
            elif "set mouse position" in text or "move mouse to specific position" in text:
                speak("Setting the mouse position to (300, 300).")
                gui.moveTo(300, 300)

            # 48
            elif "get mouse position" in text or "retrieve mouse coordinates" in text:
                speak("Getting the current mouse coordinates.")
                current_position = gui.position()
                print("Current mouse position:", current_position)

            # 49
            elif "toggle failsafe" in text or "enable failsafe" in text:
                speak("Enabling the failsafe feature.")
                gui.FAILSAFE = True

            # 50
            elif "disable failsafe" in text or "turn off failsafe" in text:
                speak("Disabling the failsafe feature.")
                gui.FAILSAFE = False

            # 51
            elif "mouse move karo" in text or "cursor move karo" in text:
                speak("Mouse ko screen ke center me move kar raha hoon.")
                gui.moveTo(gui.size()[0] / 2, gui.size()[1] / 2)

            # 52
            elif "double click karo" in text or "double click perform karo" in text:
                speak("Double-click perform kar raha hoon.")
                gui.doubleClick()

            # 53
            elif "right click karo" in text or "right click perform karo" in text:
                speak("Right-click perform kar raha hoon.")
                gui.rightClick()

            # 54
            elif "scroll neeche karo" in text or "page neeche scroll karo" in text:
                speak("Page neeche scroll kar raha hoon.")
                gui.scroll(-1)

            # 55
            elif "message likho" in text or "text likho" in text:
                speak("Ek sample message likh raha hoon.")
                gui.typewrite("Hello, PyAutoGUI!")

            # 56
            elif "enter daba do" in text or "enter key daba do" in text:
                speak("Enter key daba raha hoon.")
                gui.press("enter")

            # 57
            elif "space daba do" in text or "spacebar daba do" in text:
                speak("Spacebar daba raha hoon.")
                gui.press("space")

            # 58
            elif "tab daba do" in text or "tab key daba do" in text:
                speak("Tab key daba raha hoon.")
                gui.press("tab")

            # 59
            elif "esc daba do" in text or "esc key daba do" in text:
                speak("Esc key daba raha hoon.")
                gui.press("esc")

            # 60
            elif "screenshot le lo" in text or "screen capture karo" in text:
                speak("Screenshot le raha hoon.")
                gui.screenshot("screenshot.png")

            # 61
            elif "image dhundo" in text or "screen par image ka pata lagao" in text:
                speak("Screen par ek sample image ka location dhoond raha hoon.")
                coordinates = gui.locateOnScreen("sample_image.png")
                print("Image mila at:", coordinates)

            # 62
            elif "caps lock toggle karo" in text or "caps lock on karo" in text:
                speak("Caps Lock ko toggle kar raha hoon.")
                gui.press("capslock")

            # 63
            elif "key dabaye rakho" in text or "key ko pressed rakho" in text:
                speak("'A' key ko dabaye rakha raha hoon.")
                gui.keyDown("a")

            # 64
            elif "key chhodo" in text or "key ko chhodo" in text:
                speak("'A' key ko chhod raha hoon.")
                gui.keyUp("a")

            # 65
            elif "mouse ki speed badlo" in text or "mouse ki sensitivity adjust karo" in text:
                speak("Mouse ki speed ko 2x kar raha hoon.")
                gui.mouseInfo = (2, gui.mouseInfo[1])

            # 66
            elif "calculator kholo" in text or "calculator launch karo" in text:
                speak("Calculator khol raha hoon.")
                gui.hotkey("win", "r")
                gui.typewrite("calc")
                gui.press("enter")

            # 67
            elif "text copy karo" in text or "clipboard par copy karo" in text:
                speak("Sample text ko clipboard par copy kar raha hoon.")
                gui.typewrite("Copy this text to clipboard.")
                gui.hotkey("ctrl", "c")

            # 68
            elif "text paste karo" in text or "clipboard se paste karo" in text:
                speak("Clipboard se text paste kar raha hoon.")
                gui.hotkey("ctrl", "v")

            # 69
            elif "undo karo" in text or "undo action karo" in text:
                speak("Last action ko undo kar raha hoon.")
                gui.hotkey("ctrl", "z")

            # 70
            elif "redo karo" in text or "redo action karo" in text:
                speak("Last undone action ko redo kar raha hoon.")
                gui.hotkey("ctrl", "y")

            # 71
            elif "text cut karo" in text or "clipboard par cut karo" in text:
                speak("Sample text ko clipboard par cut kar raha hoon.")
                gui.hotkey("ctrl", "x")

            # 72
            elif "select all karo" in text or "document ka pura text select karo" in text:
                speak("Document me saara text select kar raha hoon.")
                gui.hotkey("ctrl", "a")

            # 73
            elif "file save karo" in text or "current document save karo" in text:
                speak("Current document ko save kar raha hoon.")
                gui.hotkey("ctrl", "s")

            # 74
            elif "document print karo" in text or "current page print karo" in text:
                speak("Current document ko print kar raha hoon.")
                gui.hotkey("ctrl", "p")

            # 75
            elif "text find karo" in text or "search for text karo" in text:
                speak("Text search ke liye find dialog open kar raha hoon.")
                gui.hotkey("ctrl", "f")

            # 76
            elif "new tab kholo" in text or "new browser tab launch karo" in text:
                speak("New browser tab khol raha hoon.")
                gui.hotkey("ctrl", "t")

            # 77
            elif "tab band karo" in text or "current tab band karo" in text:
                speak("Current browser tab band kar raha hoon.")
                gui.hotkey("ctrl", "w")

            # 78
            elif "tab switch karo" in text or "next tab me jao" in text:
                speak("Next browser tab me switch kar raha hoon.")
                gui.hotkey("ctrl", "tab")

            # 79
            elif "back jao" in text or "navigate back karo" in text:
                speak("Previous page me navigate kar raha hoon.")
                gui.hotkey("alt", "left")

            # 80
            elif "forward jao" in text or "navigate forward karo" in text:
                speak("Next page me navigate kar raha hoon.")
                gui.hotkey("alt", "right")

            # 81
            elif "zoom in karo" in text or "current page me zoom badhao" in text:
                speak("Current page par zoom in kar raha hoon.")
                gui.hotkey("ctrl", "+")

            # 82
            elif "zoom out karo" in text or "current page me zoom ghatao" in text:
                speak("Current page par zoom out kar raha hoon.")
                gui.hotkey("ctrl", "-")

            # 83
            elif "zoom reset karo" in text or "default zoom restore karo" in text:
                speak("Zoom level ko default par reset kar raha hoon.")
                gui.hotkey("ctrl", "0")

            # 84
            elif "settings kholo" in text or "settings launch karo" in text:
                speak("Application ke settings open kar raha hoon.")
                gui.hotkey("ctrl", ",")

            # 85
            elif "fullscreen toggle karo" in text or "fullscreen mode me jao" in text:
                speak("Fullscreen mode ko toggle kar raha hoon.")
                gui.hotkey("f11")

            # 86
            elif "dark mode toggle karo" in text or "dark theme toggle karo" in text:
                speak("Dark mode ko toggle kar raha hoon.")
                gui.hotkey("ctrl", "shift", "e")

            # 87
            elif "mute karo" in text or "tab ko mute karo" in text:
                speak("Tab ko mute kar raha hoon.")
                gui.hotkey("ctrl", "m")

            # 88
            elif "region ka screenshot lelo" in text or "specific area ka capture karo" in text:
                speak("Specific area ka screenshot le raha hoon.")
                region = (100, 100, 300, 300)  # Example region coordinates (left, top, width, height)
                gui.screenshot("region_screenshot.png", region=region)

            # 89
            elif "coordinates par click karo" in text or "position par click karo" in text:
                speak("Specific coordinates par click kar raha hoon.")
                gui.click(200, 200)

            # 90
            elif "coordinates par right click karo" in text or "position par right click karo" in text:
                speak("Specific coordinates par right-click kar raha hoon.")
                gui.rightClick(200, 200)

            # 91
            elif "coordinates par double click karo" in text or "position par double click karo" in text:
                speak("Specific coordinates par double-click kar raha hoon.")
                gui.doubleClick(200, 200)

            # 92
            elif "mouse relative move karo" in text or "cursor offset me move karo" in text:
                speak("Mouse ko current position ke relative me move kar raha hoon.")
                gui.move(50, 50, duration=1)

            # 93
            elif "scroll up karo" in text or "page upar scroll karo" in text:
                speak("Page upar scroll kar raha hoon.")
                gui.scroll(1)

            # 94
            elif "key press simulate karo" in text or "kisi key ko press karo" in text:
                speak("'A' key ko simulate kar raha hoon.")
                gui.press("a")

            # 95
            elif "key sequence press simulate karo" in text or "kisi key sequence ko press karo" in text:
                speak("Key sequence 'Ctrl+A' ko simulate kar raha hoon.")
                gui.hotkey("ctrl", "a")

            # 96
            elif "special characters type karo" in text or "symbols type karo" in text:
                speak("Special characters type kar raha hoon: @#$%^&*()")
                gui.typewrite("@#$%^&*()")

            # 97
            elif "mouse position set karo" in text or "mouse ko specific position par set karo" in text:
                speak("Mouse position ko (300, 300) par set kar raha hoon.")
                gui.moveTo(300, 300)

            # 98
            elif "mouse position get karo" in text or "mouse coordinates retrieve karo" in text:
                speak("Current mouse coordinates get kar raha hoon.")
                current_position = gui.position()
                print("Current mouse position:", current_position)

            # 99
            elif "failsafe toggle karo" in text or "failsafe feature enable karo" in text:
                speak("Failsafe feature ko enable kar raha hoon.")
                gui.FAILSAFE = True

            # 100
            elif "failsafe disable karo" in text or "failsafe feature turn off karo" in text:
                speak("Failsafe feature ko disable kar raha hoon.")
                gui.FAILSAFE = False
            # 101
            elif "text file banao" in text or "new text document create karo" in text:
                speak("Naya text document bana raha hoon.")
                gui.hotkey("ctrl", "shift", "n")

            # 102
            elif "folder banao" in text or "new folder create karo" in text:
                speak("Naya folder bana raha hoon.")
                gui.hotkey("ctrl", "shift", "n")

            # 103
            elif "screen lock karo" in text or "computer ko lock karo" in text:
                speak("Computer ko lock kar raha hoon.")
                gui.hotkey("win", "l")

            # 104
            elif "bluetooth chalu karo" in text or "bluetooth on karo" in text:
                speak("Bluetooth ko chalu kar raha hoon.")
                # Replace the following line with the appropriate command to turn on Bluetooth.

            # 105
            elif "bluetooth band karo" in text or "bluetooth off karo" in text:
                speak("Bluetooth ko band kar raha hoon.")
                # Replace the following line with the appropriate command to turn off Bluetooth.

            # 106
            elif "wi-fi chalu karo" in text or "wi-fi on karo" in text:
                speak("Wi-Fi ko chalu kar raha hoon.")
                # Replace the following line with the appropriate command to turn on Wi-Fi.

            # 107
            elif "wi-fi band karo" in text or "wi-fi off karo" in text:
                speak("Wi-Fi ko band kar raha hoon.")
                # Replace the following line with the appropriate command to turn off Wi-Fi.

            # 108
            elif "volume badhao" in text or "sound volume increase karo" in text:
                speak("Sound volume badha raha hoon.")
                gui.press("volumeup")

            # 109
            elif "volume kam karo" in text or "sound volume decrease karo" in text:
                speak("Sound volume kam kar raha hoon.")
                gui.press("volumedown")

            # 110
            elif "mute karo" in text or "sound mute karo" in text:
                speak("Sound mute kar raha hoon.")
                gui.press("volumemute")

            # 111
            elif "brightness badhao" in text or "screen brightness increase karo" in text:
                speak("Screen brightness badha raha hoon.")
                # Replace the following line with the appropriate command to increase screen brightness.

            # 112
            elif "brightness kam karo" in text or "screen brightness decrease karo" in text:
                speak("Screen brightness kam kar raha hoon.")
                # Replace the following line with the appropriate command to decrease screen brightness.

            # 113
            elif "camera chalu karo" in text or "webcam on karo" in text:
                speak("Webcam ko chalu kar raha hoon.")
                # Replace the following line with the appropriate command to turn on the webcam.

            # 114
            elif "camera band karo" in text or "webcam off karo" in text:
                speak("Webcam ko band kar raha hoon.")
                # Replace the following line with the appropriate command to turn off the webcam.

            # 115
            elif "file copy karo" in text or "document ko copy karo" in text:
                speak("Document ko clipboard par copy kar raha hoon.")
                gui.hotkey("ctrl", "c")

            # 116
            elif "file paste karo" in text or "document ko paste karo" in text:
                speak("Clipboard se document paste kar raha hoon.")
                gui.hotkey("ctrl", "v")

            # 117
            elif "file cut karo" in text or "document ko cut karo" in text:
                speak("Document ko clipboard par cut kar raha hoon.")
                gui.hotkey("ctrl", "x")

            # 118
            elif "file delete karo" in text or "document ko delete karo" in text:
                speak("Document ko delete kar raha hoon.")
                gui.press("delete")

            # 119
            elif "file undo karo" in text or "document me undo karo" in text:
                speak("Last action ko undo kar raha hoon.")
                gui.hotkey("ctrl", "z")

            # 120
            elif "file redo karo" in text or "document me redo karo" in text:
                speak("Last undone action ko redo kar raha hoon.")
                gui.hotkey("ctrl", "y")

            # 121
            elif "file select all karo" in text or "document ka pura text select karo" in text:
                speak("Document me saara text select kar raha hoon.")
                gui.hotkey("ctrl", "a")

            # 122
            elif "file save karo" in text or "document ko save karo" in text:
                speak("Document ko save kar raha hoon.")
                gui.hotkey("ctrl", "s")

            # 123
            elif "file print karo" in text or "document ko print karo" in text:
                speak("Document ko print kar raha hoon.")
                gui.hotkey("ctrl", "p")

            # 124
            elif "file find karo" in text or "document me text search karo" in text:
                speak("Text search ke liye find dialog open kar raha hoon.")
                gui.hotkey("ctrl", "f")

            # 125
            elif "browser kholo" in text or "web browser open karo" in text:
                speak("Web browser khol raha hoon.")
                gui.hotkey("ctrl", "t")

            # 126
            elif "current tab band karo" in text or "current browser tab close karo" in text:
                speak("Current browser tab band kar raha hoon.")
                gui.hotkey("ctrl", "w")

            # 127
            elif "next tab me jao" in text or "next browser tab me switch karo" in text:
                speak("Next browser tab me switch kar raha hoon.")
                gui.hotkey("ctrl", "tab")

            # 128
            elif "previous page me jao" in text or "previous page me navigate karo" in text:
                speak("Previous page me navigate kar raha hoon.")
                gui.hotkey("alt", "left")

            # 129
            elif "next page me jao" in text or "next page me navigate karo" in text:
                speak("Next page me navigate kar raha hoon.")
                gui.hotkey("alt", "right")

            # 130
            elif "current page par zoom in karo" in text or "current page ko zoom in karo" in text:
                speak("Current page par zoom in kar raha hoon.")
                gui.hotkey("ctrl", "+")

            # 131
            elif "current page par zoom out karo" in text or "current page ko zoom out karo" in text:
                speak("Current page par zoom out kar raha hoon.")
                gui.hotkey("ctrl", "-")

            # 132
            elif "current page ka zoom reset karo" in text or "current page ka zoom reset karo" in text:
                speak("Current page ka zoom level reset kar raha hoon.")
                gui.hotkey("ctrl", "0")

            # 133
            elif "settings kholo" in text or "application ke settings open karo" in text:
                speak("Application ke settings open kar raha hoon.")
                gui.hotkey("ctrl", ",")

            # 134
            elif "fullscreen mode toggle karo" in text or "fullscreen mode ko toggle karo" in text:
                speak("Fullscreen mode ko toggle kar raha hoon.")
                gui.hotkey("f11")

            # 135
            elif "dark mode toggle karo" in text or "dark theme toggle karo" in text:
                speak("Dark mode ko toggle kar raha hoon.")
                gui.hotkey("ctrl", "shift", "e")

            # 136
            elif "tab ko mute karo" in text or "current tab ko mute karo" in text:
                speak("Current tab ko mute kar raha hoon.")
                gui.hotkey("ctrl", "m")

            # 137
            elif "specific area ka screenshot lelo" in text or "specific region ka screenshot capture karo" in text:
                speak("Specific region ka screenshot le raha hoon.")
                region = (100, 100, 300, 300)  # Example region coordinates (left, top, width, height)
                gui.screenshot("region_screenshot.png", region=region)

            # 138
            elif "specific position par click karo" in text or "specific coordinates par click karo" in text:
                speak("Specific coordinates par click kar raha hoon.")
                gui.click(200, 200)

            # 139
            elif "specific position par right click karo" in text or "specific coordinates par right click karo" in text:
                speak("Specific coordinates par right-click kar raha hoon.")
                gui.rightClick(200, 200)

            # 140
            elif "specific position par double click karo" in text or "specific coordinates par double click karo" in text:
                speak("Specific coordinates par double-click kar raha hoon.")
                gui.doubleClick(200, 200)

            # 141
            elif "mouse ko relative me move karo" in text or "mouse ko offset me move karo" in text:
                speak("Mouse ko current position ke relative me move kar raha hoon.")
                gui.move(50, 50, duration=1)

            # 142
            elif "page upar scroll karo" in text or "page upar scroll karo" in text:
                speak("Page upar scroll kar raha hoon.")
                gui.scroll(1)

            # 143
            elif "kisi key ko simulate karo" in text or "kisi key ko press karo" in text:
                speak("'A' key ko simulate kar raha hoon.")
                gui.press("a")

            # 144
            elif "kisi key sequence ko simulate karo" in text or "kisi key sequence ko press karo" in text:
                speak("Key sequence 'Ctrl+A' ko simulate kar raha hoon.")
                gui.hotkey("ctrl", "a")

            # 145
            elif "special characters type karo" in text or "symbols type karo" in text:
                speak("Special characters type kar raha hoon: @#$%^&*()")
                gui.typewrite("@#$%^&*()")

            # 146
            elif "mouse position ko set karo" in text or "mouse ko specific position par set karo" in text:
                speak("Mouse position ko (300, 300) par set kar raha hoon.")
                gui.moveTo(300, 300)

            # 147
            elif "current mouse position get karo" in text or "current mouse coordinates retrieve karo" in text:
                speak("Current mouse coordinates get kar raha hoon.")
                current_position = gui.position()
                print("Current mouse position:", current_position)

            # 148
            elif "failsafe feature ko enable karo" in text or "failsafe feature enable karo" in text:
                speak("Failsafe feature ko enable kar raha hoon.")
                gui.FAILSAFE = True

            # 149
            elif "failsafe feature ko disable karo" in text or "failsafe feature disable karo" in text:
                speak("Failsafe feature ko disable kar raha hoon.")
                gui.FAILSAFE = False
            # 150
            elif "brightness kam karo" in text or "screen brightness decrease karo" in text:
                speak("Screen brightness kam kar raha hoon.")
                # Replace the following line with the appropriate command to decrease screen brightness.

            # 151
            elif "brightness zyada karo" in text or "screen brightness increase karo" in text:
                speak("Screen brightness zyada kar raha hoon.")
                # Replace the following line with the appropriate command to increase screen brightness.

            # 152
            elif "caps lock toggle karo" in text or "caps lock on karo" in text:
                speak("Caps Lock ko toggle kar raha hoon.")
                gui.press("capslock")

            # 153
            elif "num lock toggle karo" in text or "num lock on karo" in text:
                speak("Num Lock ko toggle kar raha hoon.")
                gui.press("numlock")

            # 154
            elif "number dalo" in text or "numeric value type karo" in text:
                speak("Numeric value type kar raha hoon: 12345")
                gui.typewrite("12345")

            # 155
            elif "scroll right karo" in text or "page right scroll karo" in text:
                speak("Page right scroll kar raha hoon.")
                gui.hscroll(1)

            # 156
            elif "scroll left karo" in text or "page left scroll karo" in text:
                speak("Page left scroll kar raha hoon.")
                gui.hscroll(-1)

            # 157
            elif "clipboard se paste karo" in text or "paste from clipboard karo" in text:
                speak("Clipboard se text paste kar raha hoon.")
                gui.hotkey("ctrl", "v")

            # 158
            elif "undo karo" in text or "last action undo karo" in text:
                speak("Last action ko undo kar raha hoon.")
                gui.hotkey("ctrl", "z")

            # 159
            elif "redo karo" in text or "last undone action redo karo" in text:
                speak("Last undone action ko redo kar raha hoon.")
                gui.hotkey("ctrl", "y")

            # 160
            elif "select all karo" in text or "document ka pura text select karo" in text:
                speak("Document me saara text select kar raha hoon.")
                gui.hotkey("ctrl", "a")

            # 161
            elif "copy karo" in text or "selected text ko clipboard par copy karo" in text:
                speak("Selected text ko clipboard par copy kar raha hoon.")
                gui.hotkey("ctrl", "c")

            # 162
            elif "paste karo" in text or "clipboard se paste karo" in text:
                speak("Clipboard se text paste kar raha hoon.")
                gui.hotkey("ctrl", "v")

            # 163
            elif "cut karo" in text or "selected text ko clipboard par cut karo" in text:
                speak("Selected text ko clipboard par cut kar raha hoon.")
                gui.hotkey("ctrl", "x")

            # 164
            elif "find karo" in text or "text search dialog open karo" in text:
                speak("Text search ke liye find dialog open kar raha hoon.")
                gui.hotkey("ctrl", "f")

            # 165
            elif "new tab kholo" in text or "new browser tab open karo" in text:
                speak("New browser tab khol raha hoon.")
                gui.hotkey("ctrl", "t")

            # 166
            elif "current tab band karo" in text or "current browser tab close karo" in text:
                speak("Current browser tab band kar raha hoon.")
                gui.hotkey("ctrl", "w")

            # 167
            elif "tab switch karo" in text or "next tab me jao" in text:
                speak("Next browser tab me switch kar raha hoon.")
                gui.hotkey("ctrl", "tab")

            # 168
            elif "back jao" in text or "navigate back karo" in text:
                speak("Previous page me navigate kar raha hoon.")
                gui.hotkey("alt", "left")

            # 169
            elif "forward jao" in text or "navigate forward karo" in text:
                speak("Next page me navigate kar raha hoon.")
                gui.hotkey("alt", "right")

            # 170
            elif "zoom in karo" in text or "current page me zoom in karo" in text:
                speak("Current page par zoom in kar raha hoon.")
                gui.hotkey("ctrl", "+")

            # 171
            elif "zoom out karo" in text or "current page me zoom out karo" in text:
                speak("Current page par zoom out kar raha hoon.")
                gui.hotkey("ctrl", "-")

            # 172
            elif "zoom reset karo" in text or "default zoom restore karo" in text:
                speak("Zoom level ko default par reset kar raha hoon.")
                gui.hotkey("ctrl", "0")

            # 173
            elif "settings kholo" in text or "application ke settings open karo" in text:
                speak("Application ke settings open kar raha hoon.")
                gui.hotkey("ctrl", ",")

            # 174
            elif "fullscreen toggle karo" in text or "fullscreen mode me jao" in text:
                speak("Fullscreen mode ko toggle kar raha hoon.")
                gui.hotkey("f11")

            # 175
            elif "dark mode toggle karo" in text or "dark theme toggle karo" in text:
                speak("Dark mode ko toggle kar raha hoon.")
                gui.hotkey("ctrl", "shift", "e")

            # 176
            elif "mute karo" in text or "tab ko mute karo" in text:
                speak("Tab ko mute kar raha hoon.")
                gui.hotkey("ctrl", "m")

            # 177
            elif "region ka screenshot lelo" in text or "specific area ka screenshot capture karo" in text:
                speak("Specific area ka screenshot le raha hoon.")
                region = (100, 100, 300, 300)  # Example region coordinates (left, top, width, height)
                gui.screenshot("region_screenshot.png", region=region)

            # 178
            elif "coordinates par click karo" in text or "position par click karo" in text:
                speak("Specific coordinates par click kar raha hoon.")
                gui.click(200, 200)

            # 179
            elif "coordinates par right click karo" in text or "position par right click karo" in text:
                speak("Specific coordinates par right-click kar raha hoon.")
                gui.rightClick(200, 200)

            # 180
            elif "coordinates par double click karo" in text or "position par double click karo" in text:
                speak("Specific coordinates par double-click kar raha hoon.")
                gui.doubleClick(200, 200)

            # 181
            elif "mouse relative move karo" in text or "cursor offset me move karo" in text:
                speak("Mouse ko current position ke relative me move kar raha hoon.")
                gui.move(50, 50, duration=1)

            # 182
            elif "scroll up karo" in text or "page upar scroll karo" in text:
                speak("Page upar scroll kar raha hoon.")
                gui.scroll(1)

            # 183
            elif "key press simulate karo" in text or "kisi key ko press karo" in text:
                speak("'A' key ko simulate kar raha hoon.")
                gui.press("a")

            # 184
            elif "key sequence press simulate karo" in text or "kisi key sequence ko press karo" in text:
                speak("Key sequence 'Ctrl+A' ko simulate kar raha hoon.")
                gui.hotkey("ctrl", "a")

            # 185
            elif "special characters type karo" in text or "symbols type karo" in text:
                speak("Special characters type kar raha hoon: @#$%^&*()")
                gui.typewrite("@#$%^&*()")

            # 186
            elif "mouse position set karo" in text or "mouse ko specific position par set karo" in text:
                speak("Mouse position ko (300, 300) par set kar raha hoon.")
                gui.moveTo(300, 300)

            # 187
            elif "mouse position get karo" in text or "mouse coordinates retrieve karo" in text:
                speak("Current mouse coordinates get kar raha hoon.")
                current_position = gui.position()
                print("Current mouse position:", current_position)

            # 188
            elif "failsafe toggle karo" in text or "failsafe feature enable karo" in text:
                speak("Failsafe feature ko enable kar raha hoon.")
                gui.FAILSAFE = True

            # 189
            elif "failsafe disable karo" in text or "failsafe feature turn off karo" in text:
                speak("Failsafe feature ko disable kar raha hoon.")
                gui.FAILSAFE = False
            # 190
            elif "create a new folder" in text or "folder banao" in text:
                speak("Creating a new folder.")
                gui.hotkey("ctrl", "shift", "n")

            # 191
            elif "lock the screen" in text or "screen lock karo" in text:
                speak("Locking the screen.")
                gui.hotkey("win", "l")


            # 195
            elif "enable Caps Lock" in text or "Caps Lock on karo" in text:
                speak("Enabling Caps Lock.")
                gui.press("capslock")

            # 196
            elif "disable Caps Lock" in text or "Caps Lock off karo" in text:
                speak("Disabling Caps Lock.")
                gui.press("capslock")

            # 197
            elif "enable Num Lock" in text or "Num Lock on karo" in text:
                speak("Enabling Num Lock.")
                gui.press("numlock")

            # 198
            elif "disable Num Lock" in text or "Num Lock off karo" in text:
                speak("Disabling Num Lock.")
                gui.press("numlock")

            # 199
            elif "type the number" in text or "number dalo" in text:
                speak("Typing the number: 12345")
                gui.typewrite("12345")

            # 200
            elif "scroll to the right" in text or "right scroll karo" in text:
                speak("Scrolling to the right.")
                gui.hscroll(1)

            # 201
            elif "scroll to the left" in text or "left scroll karo" in text:
                speak("Scrolling to the left.")
                gui.hscroll(-1)

            # 202
            elif "paste from clipboard" in text or "clipboard se paste karo" in text:
                speak("Pasting from the clipboard.")
                gui.hotkey("ctrl", "v")

            # 203
            elif "undo the action" in text or "undo karo" in text:
                speak("Undoing the last action.")
                gui.hotkey("ctrl", "z")

            # 204
            elif "redo the action" in text or "redo karo" in text:
                speak("Redoing the last undone action.")
                gui.hotkey("ctrl", "y")

            # 205
            elif "select all" in text or "document ka pura text select karo" in text:
                speak("Selecting all text in the document.")
                gui.hotkey("ctrl", "a")

            # 206
            elif "copy the selected text" in text or "selected text ko copy karo" in text:
                speak("Copying the selected text to the clipboard.")
                gui.hotkey("ctrl", "c")

            # 207
            elif "paste from clipboard" in text or "clipboard se paste karo" in text:
                speak("Pasting text from the clipboard.")
                gui.hotkey("ctrl", "v")

            # 208
            elif "cut the selected text" in text or "selected text ko cut karo" in text:
                speak("Cutting the selected text to the clipboard.")
                gui.hotkey("ctrl", "x")

            # 209
            elif "find text" in text or "text search dialog open karo" in text:
                speak("Opening the text search dialog.")
                gui.hotkey("ctrl", "f")

            # 210
            elif "open a new browser tab" in text or "new tab kholo" in text:
                speak("Opening a new browser tab.")
                gui.hotkey("ctrl", "t")

            # 211
            elif "close the current browser tab" in text or "current tab band karo" in text:
                speak("Closing the current browser tab.")
                gui.hotkey("ctrl", "w")

            # 212
            elif "switch to the next browser tab" in text or "tab switch karo" in text:
                speak("Switching to the next browser tab.")
                gui.hotkey("ctrl", "tab")

            # 213
            elif "navigate back" in text or "back jao" in text:
                speak("Navigating back to the previous page.")
                gui.hotkey("alt", "left")

            # 214
            elif "navigate forward" in text or "forward jao" in text:
                speak("Navigating forward to the next page.")
                gui.hotkey("alt", "right")

            # 215
            elif "zoom in on the current page" in text or "current page me zoom in karo" in text:
                speak("Zooming in on the current page.")
                gui.hotkey("ctrl", "+")

            # 216
            elif "zoom out on the current page" in text or "current page me zoom out karo" in text:
                speak("Zooming out on the current page.")
                gui.hotkey("ctrl", "-")

            # 217
            elif "reset the zoom level" in text or "zoom reset karo" in text:
                speak("Resetting the zoom level to default.")
                gui.hotkey("ctrl", "0")

            elif "scroll up on the page" in text or "page upar scroll karo" in text:
                speak("Scrolling up on the page.")
                gui.scroll(1)

            elif "working on new project" in text or "lets start new project" in text or "create new project" in text :
                project_creator()

            elif "open" in text:
                Nameoftheapp = text.replace("open ", "")
                speak(f"opening {Nameoftheapp}")
                pyautogui.press('win')
                time.sleep(1)
                keyboard.write(Nameoftheapp)
                time.sleep(1)
                keyboard.press('enter')
                time.sleep(0.5)


# Start all threads
thread1 = threading.Thread(target=battery_alert)
thread2 = threading.Thread(target=main)
thread3 = threading.Thread(target=check_plugin_status)
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()