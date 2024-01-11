import time
import pyautogui as gui
import pywhatkit as kit
from Body.speak import speak
from Body.listen import hearing
import random


def whatsapp_call(name):
    gui.press("win")
    time.sleep(1)
    gui.write("whatsapp")
    time.sleep(1)
    gui.press("enter")
    time.sleep(2)
    gui.write(name)
    time.sleep(2)
    gui.hotkey("down")
    time.sleep(2)

    gui.press("enter")




def Send_massege_on_Whatsapp():
    dlg = [
        "To whom shall I send the message, sir?",
        "May I inquire about the intended recipient, sir?",
        "Sir, kindly specify the person you wish to message.",
        "For whom is the message intended, sir?",
        "Could you please provide the name of the recipient, sir?",
        "Sir, who is the intended recipient for the message?",
        "Shall I ask for the name of the person you're messaging, sir?",
        "Sir, may I know the name of the recipient for the message?",
        "Who is the intended recipient of the message, sir?",
        "To which contact should I address the message, sir?",
        "For which contact should I send the message, sir?",
        "Sir, please specify the name of the recipient for the message.",
        "Whose message would you like to send, sir?",
        "Sir, kindly mention the name of the person you're messaging.",
        "May I have the recipient's name for the message, sir?",
        "To whom should I direct the message, sir?",
        "What is the name of the person you want to message, sir?",
        "Could you tell me the intended recipient, sir?",
        "Sir, for whom is the message intended?",
        "Who would you like to send the message to, sir?",
        "Sir, please provide the name of the person for the message.",
        "What's the name of the recipient, sir?",
        "May I know the name of the person you're messaging, sir?",
        "Which contact should I select for the message, sir?",
        "Sir, kindly mention the recipient's name for the message.",
        "Who's the intended recipient of the message, sir?",
        "For which contact should I compose the message, sir?",
        "To whom should I address the message, sir?",
        "Sir, please specify the name of the recipient for the message.",
        "May I inquire about the intended recipient's name, sir?",
        "Who is the message for, sir?",
        "What is the name of the person you want to send the message to, sir?",
        "Sir, could you please provide the name of the recipient?",
        "Which contact is the message intended for, sir?",
        "For whom shall I compose the message, sir?",
        "To which contact should I send the message, sir?",
        "Who is the intended receiver of the message, sir?",
        "What's the name of the person you're sending the message to, sir?",
        "May I have the recipient's name for the message, sir?",
        "Sir, for whom would you like to send the message?",
        "Could you please specify the recipient's name, sir?",
        "Who is the message addressed to, sir?",
        "To whom would you like me to send the message, sir?",
        "What is the name of the recipient for the message, sir?",
        "Sir, please provide the name of the person you're messaging.",
        "May I know the name of the person you're sending the message to, sir?",
        "Which contact should I select for the message, sir?",
        "Sir, kindly mention the recipient's name for the message.",
        "Who's the intended recipient of the message, sir?",
        "For which contact should I compose the message, sir?",

    ]
    repdlg = random.choice(dlg)
    speak(repdlg)
    contact_name = hearing().lower()

    if contact_name == "papa":
        contact_name = "+918226098666"

    elif contact_name == "girlfriend":
        contact_name = "+919413512895"
    # Get the message to send
    speak("what i should i send sir ")
    message = hearing().lower()

    # Get the current time

    # Send the message
    kit.sendwhatmsg_instantly(f"{contact_name}", f"{message}", wait_time=15, tab_close=True)

    speak(f"Messege sent successfully")


def Send_massege_on_Whatsapp2():
    # Get the name of the contact

    # speak("who do you want to massege sir")
    contact_name = "papa"

    if contact_name == "papa":
        contact_name = "+918226098666"

    elif contact_name == "girlfriend":
        contact_name = "+919413512895"
    # Get the message to send
    # speak("what i should i send sir ")
    message = "GOOD NIGHT PAPA JI OR MUMMY JI ! JAY SHREE RAM ! RADHEY RADHEY !"
    # Get the current time

    # Send the message
    kit.sendwhatmsg_instantly(f"{contact_name}", f"{message}", wait_time=8, tab_close=True)

    speak(f"Messege sent successfully")


def Send_massege_on_Whatsapp3():
    # Get the name of the contact

    # speak("who do you want to massege sir")
    contact_name = "girlfriend"

    if contact_name == "papa":
        contact_name = "+918226098666"

    elif contact_name == "girlfriend":
        contact_name = "+919413512895"
    # Get the message to send
    # speak("what i should i send sir "
    responses = ["GOOD NIGHT ! SLEEP WELL ! TAKE CARE ! RADHEY RADHEY !", "Good night ,Sweet dreams ! RADHEY RADHEY !",
                 "good night ! RADHEY RADHEY ! TAKE CARE ! SLEEP WELL",
                 "GOOD NIGHT ! RADHEY RADHEY ! i will meet you new dream world"]
    response = random.choice(responses)

    message = response
    # Get the current time

    # Send the message
    kit.sendwhatmsg_instantly(f"{contact_name}", f"{message}", wait_time=8, tab_close=True)

    speak(f"Messege sent successfully")






