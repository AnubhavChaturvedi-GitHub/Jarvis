import tkinter as tk
import time
import imaplib
import email
import datetime
from PIL import Image, ImageTk


def showMassege():
    # Connect to the IMAP server
    imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
    imap_server.login('chaturvedianubhav520@gmail.com', 'muyg nzrj fsju jhzp')

    # Select the mailbox you want to check (e.g. "inbox")
    mailbox = 'inbox'
    imap_server.select(mailbox)

    # Search for new unread emails
    status, email_ids = imap_server.search(None, 'UNSEEN')

    # Get the latest 3 email IDs
    latest_email_ids = email_ids[0].split()[-3:]

    # Create a message string to display the email information
    message = ""

    # Iterate over the list of email IDs and fetch each email
    for email_id in latest_email_ids:
        message += "\n-------------------------------------------------------------\n"
        # Fetch the email data
        status, email_data = imap_server.fetch(email_id, '(RFC822)')

        # Parse the email data into an EmailMessage object
        email_message = email.message_from_bytes(email_data[0][1])

        # Get the date and time of the email
        email_datetime = datetime.datetime.strptime(email_message['Date'], '%a, %d %b %Y %H:%M:%S %z (%Z)')

        # Format the date and time string
        time_string = email_datetime.strftime('%I:%M %p')

        # Add the email information to the message string
        message += f"From: {email_message['From']}\n"
        message += f"Date: {email_datetime.strftime('%m/%d/%Y')}\n"
        message += f"Time: {time_string}\n"
        message += f"Subject: {email_message['Subject']}\n"

    for i in range(len(message)):
        message_label.config(text=message[:i + 1])
        time.sleep(0.03)
        window.update()
    message_label.config(text=message)


# Create a window
window = tk.Tk()
window.title("Check your emails")
# window.configure(bg="black")  # set the background color to black
# Add a background image to the window
bg_image = Image.open("/home/mr_zenox/Desktop/Jarvis/imageData/jarvisbg2.png")
bg_image = bg_image.resize((800, 600), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0)

# Make sure to keep a reference to the photo image to avoid garbage collection
bg_label.image = bg_photo

# Set the window size
window.geometry("700x600")

# Add a label to display the message
message_label = tk.Label(window, text="", fg="light green", bg="black", font=("Helvetica", 16), wraplength=700)
message_label.place(x=0, y=250, anchor="w")

# Call showMassege function to print message
showMassege()

# Start the GUI loop
window.mainloop()