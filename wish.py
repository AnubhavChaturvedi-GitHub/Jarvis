import datetime
from datetime import date
from Body.speak import speak
import random
from Works.temp import Temp
from Works.cloud_weather import *
today = date.today()
formatted_date = today.strftime("%d %b %Y")

nowx = datetime.datetime.now()

def random_morning_greeting():
    good_morning_wish = [
        "Good to see you again, sir. Very good morning! May your day be as bright as the sunrise.",
        "Hello, sir! Wishing you a morning filled with positivity and new possibilities. Good morning!",
        "Top of the morning to you, sir! May your day unfold like a beautiful story.",
        "Rise and shine, sir! Good morning! May the day ahead be filled with joy and success.",
        "A bright and cheerful morning, sir! May your day be as vibrant as the morning sun.",
        "Greetings, sir! Have a fantastic morning! Wishing you moments of peace and productivity.",
        "Wishing you a day filled with positivity, sir! Good morning and may success follow you.",
        "Good morning, sir! May your day be great and filled with accomplishments.",
        "Hello, sir! Starting the day with a warm greeting! May your morning set the tone for a wonderful day.",
        "A pleasant morning to you, sir! May the day ahead bring you joy and fulfillment.",
        "Good morning, sir! Wishing you a day filled with inspiration and positive vibes.",
        "Hello, sir! May your morning be as refreshing as the first sip of coffee. Good morning!",
        "Top of the morning to you, sir! May your day be productive and rewarding.",
        "Rise and shine, sir! Good morning! Embrace the opportunities this new day brings.",
        "A bright and cheerful morning, sir! May your day be as lively as your spirit.",
        "Greetings, sir! Have a fantastic morning! May your day be filled with laughter and success.",
        "Wishing you a day filled with positivity, sir! Good morning and make the most of today.",
        "Good morning, sir! May the sunrise bring you hope and the day ahead, fulfillment.",
        "Hello, sir! Starting the day with a warm greeting! May your morning be the beginning of something extraordinary.",
        "A pleasant morning to you, sir! May the day unfold with ease and grace.",
        "Good morning, sir! Wishing you a day filled with creativity and accomplishment.",
        "Top of the morning to you, sir! May your day be as bright as your smile.",
        "Rise and shine, sir! Good morning! May today be a step closer to your goals.",
        "A bright and cheerful morning, sir! Embrace the positivity the morning brings.",
        "Greetings, sir! Have a fantastic morning! May your day be filled with positive surprises.",
        "Wishing you a day filled with positivity, sir! Good morning and may success be your companion.",
        "Good morning, sir! May your day be great and full of exciting possibilities.",
        "Hello, sir! Starting the day with a warm greeting! May your morning be a preview of a wonderful day.",
        "A pleasant morning to you, sir! May your day be as promising as the dawn.",
        "Good morning, sir! Wishing you a day filled with inspiration and positive energy.",
        "Top of the morning to you, sir! May your day be productive and filled with accomplishments.",
        "Rise and shine, sir! Good morning! Seize the opportunities that come your way.",
        "A bright and cheerful morning, sir! May your day be as lively as your spirit.",
        "Greetings, sir! Have a fantastic morning! May your efforts be rewarded today.",
        "Wishing you a day filled with positivity, sir! Good morning and make the most of every moment.",
        "Good morning, sir! May the sunrise bring you hope and set a positive tone for the day.",
        "Hello, sir! Starting the day with a warm greeting! May your morning be the beginning of something extraordinary.",
        "A pleasant morning to you, sir! May the day unfold with ease and grace.",
        "Good morning, sir! Wishing you a day filled with creativity and accomplishment.",
        "Top of the morning to you, sir! May your day be as bright as your smile.",
        "Rise and shine, sir! Good morning! May today be a step closer to your goals.",
        "A bright and cheerful morning, sir! Embrace the positivity the morning brings.",
        "Greetings, sir! Have a fantastic morning! May your day be filled with positive surprises.",
        "Wishing you a day filled with positivity, sir! Good morning and may success be your companion.",
        "Good morning, sir! May your day be great and full of exciting possibilities.",
        "Hello, sir! Starting the day with a warm greeting! May your morning be a preview of a wonderful day.",
        "A pleasant morning to you, sir! May your day be as promising as the dawn.",
        "Good morning, sir! Wishing you a day filled with inspiration and positive energy.",
        "Top of the morning to you, sir! May your day be productive and filled with accomplishments.",
        "Rise and shine, sir! Good morning! Seize the opportunities that come your way."
    ]
    selected_greeting = random.choice(good_morning_wish)
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(f"{selected_greeting}, the time is {current_time}")
    speak(selected_greeting)
    speak(f"it's {current_time}")
    Temp()
    rep()



def random_afternoon_greeting():
    good_afternoon_wish = [
        "Good afternoon, sir! Hope the day has been treating you exceptionally well so far.",
        "Hello, sir! Wishing you a peaceful and pleasant afternoon filled with positive moments.",
        "Afternoon greetings, sir! May the remainder of your day continue to be as wonderful as the morning.",
        "Good day, sir! Sending waves of positive vibes your way this beautiful afternoon!",
        "Hello, sir! Trust you're enjoying the warmth of the afternoon sunshine. Wishing you a delightful day.",
        "Good afternoon, sir! Keep up the fantastic work; your efforts are truly appreciated.",
        "Afternoon, sir! Wishing you continued success in all your endeavors as the day unfolds.",
        "Greetings, sir! Hope your afternoon is as bright and fulfilling as your morning has been.",
        "Hello, sir! Just checking in to wish you a fantastic afternoon filled with productivity and joy.",
        "Good afternoon, sir! Keep smiling and shining; your positivity makes a difference.",
        "Good afternoon, sir! May the midday break bring you renewed energy for the rest of the day.",
        "Hello, sir! Wishing you a productive and positive afternoon ahead. Keep up the great work!",
        "Afternoon greetings, sir! Take a moment to breathe and embrace the opportunities this afternoon holds.",
        "Good day, sir! Sending you warm wishes for a relaxing and enjoyable afternoon.",
        "Hello, sir! May the afternoon breeze carry away any stress, leaving behind tranquility and focus.",
        "Good afternoon, sir! Your dedication and hard work are truly commendable. Keep going strong!",
        "Afternoon, sir! Wishing you success in every task and project you're undertaking today.",
        "Greetings, sir! Hope your afternoon is filled with positive interactions and achievements.",
        "Hello, sir! Take a moment to appreciate your accomplishments and recharge for the rest of the day. Good afternoon!",
        "Good afternoon, sir! Your enthusiasm is contagious; keep spreading positivity.",
        "Afternoon greetings, sir! May the afternoon be a canvas for new opportunities and successes.",
        "Good day, sir! Wishing you a harmonious and productive afternoon. Your efforts are truly valued.",
        "Hello, sir! Embrace the challenges of the afternoon, knowing that you have the skills to overcome them.",
        "Good afternoon, sir! Take a brief pause to appreciate the progress you've made so far today.",
        "Afternoon, sir! Your commitment to excellence is inspiring. Wishing you continued success.",
        "Greetings, sir! Hope your afternoon is unfolding smoothly, filled with positive moments.",
        "Hello, sir! Take a moment to savor the achievements of the morning and gear up for a successful afternoon.",
        "Good afternoon, sir! Your dedication and resilience are truly commendable. Keep up the great work!",
        "Afternoon, sir! Wishing you joy and accomplishment in every task you undertake.",
        "Greetings, sir! May the afternoon be a continuation of the positive momentum you've built throughout the day.",
        "Hello, sir! Take a moment to recharge and refocus as you navigate through the tasks of the afternoon. Good afternoon!",
        "Good afternoon, sir! Your hard work is making a significant impact. Keep pushing towards your goals.",
        "Afternoon greetings, sir! Wishing you a fulfilling and successful afternoon as you pursue your endeavors.",
        "Hello, sir! May the afternoon bring you fresh ideas and opportunities for growth. Keep shining!",
        "Good afternoon, sir! Your dedication and commitment are setting the tone for a successful day. Keep up the excellent work!",
        "Afternoon, sir! Wishing you continued inspiration and achievement in all your endeavors.",
        "Greetings, sir! Hope your afternoon is filled with positive experiences and successful outcomes.",
        "Hello, sir! Take a moment to appreciate the progress you've made so far today. Good afternoon!",
        "Good afternoon, sir! Your perseverance is truly commendable. Wishing you a rewarding and productive afternoon.",
        "Afternoon, sir! Your positive impact is felt throughout the day. Keep spreading inspiration.",
        "Hello, sir! Wishing you a serene and productive afternoon filled with success and accomplishment.",
        "Good afternoon, sir! May the remainder of your day be filled with positivity and successful endeavors.",
        "Afternoon greetings, sir! Your commitment to excellence is truly admirable. Keep making a difference.",
        "Greetings, sir! Hope your afternoon is unfolding smoothly, filled with positive moments and achievements.",
        "Hello, sir! Take a moment to recharge and refocus as you navigate through the tasks of the afternoon. Good afternoon!",
        "Good afternoon, sir! Your hard work is making a significant impact. Keep pushing towards your goals.",
        "Afternoon, sir! Wishing you joy and accomplishment in every task you undertake.",
        "Greetings, sir! May the afternoon be a continuation of the positive momentum you've built throughout the day.",
        "Hello, sir! May the afternoon bring you fresh ideas and opportunities for growth. Keep shining!",
        "Good afternoon, sir! Your dedication and commitment are setting the tone for a successful day. Keep up the excllent work!"
    ]
    selected_greeting = random.choice(good_afternoon_wish)
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(f"{selected_greeting}, the time is {current_time}")
    speak(selected_greeting)
    speak(f"it's, {current_time}")
    Temp()
    rep()



def random_evening_greeting():
    good_evening_wish = [
        "Good evening, sir! Wishing you a tranquil and rejuvenating evening ahead.",
        "Hello, sir! As the day winds down, may your evening be filled with moments of joy and relaxation.",
        "Evening greetings, sir! Take a moment to unwind and enjoy the serenity of the evening.",
        "Good evening, sir! Reflect on the achievements of the day as you embrace the peaceful night.",
        "Hello, sir! Wishing you a pleasant and serene evening filled with positive vibes.",
        "Evening, sir! May your night be as calm and beautiful as the evening sky above.",
        "Good evening, sir! Take a break, step back, and enjoy the beauty that the evening brings.",
        "Greetings, sir! Hope you have a delightful evening ahead, filled with moments of joy.",
        "Hello, sir! Evening is a time to recharge and relax. May you find tranquility and comfort.",
        "Good evening, sir! May the night bring you peace and happiness as you unwind from the day.",
        "Hello, sir! As the sun sets, may your worries fade, and your evening be filled with contentment.",
        "Evening greetings, sir! Take this time to appreciate the beauty that surrounds you in the evening.",
        "Good evening, sir! Wishing you a calm and enjoyable evening as you wrap up the day.",
        "Hello, sir! As the day bids farewell, may your evening be filled with serenity and positivity.",
        "Evening, sir! Take a moment to pause and enjoy the quiet beauty of the evening hours.",
        "Good evening, sir! May your evening be as delightful as the company you keep and the moments you cherish.",
        "Greetings, sir! Embrace the peaceful ambiance of the evening as you unwind and relax.",
        "Hello, sir! Wishing you a restful and enjoyable evening surrounded by warmth and comfort.",
        "Good evening, sir! Take this time to appreciate the accomplishments of the day and look forward to a tranquil night.",
        "Evening, sir! As the day gracefully concludes, may your evening unfold with peace and satisfaction.",
        "Hello, sir! May your evening be a canvas painted with moments of serenity and happiness.",
        "Good evening, sir! Wishing you a delightful and peaceful evening filled with positivity.",
        "Evening greetings, sir! Take a deep breath and savor the calmness that the evening brings.",
        "Hello, sir! As the day transitions to evening, may your surroundings be filled with peace and serenity.",
        "Good evening, sir! Reflect on the triumphs of the day as you ease into a relaxing evening.",
        "Greetings, sir! Hope your evening is a serene interlude, preparing you for a peaceful night.",
        "Hello, sir! Wishing you a tranquil evening filled with relaxation and moments of joy.",
        "Evening, sir! Take a pause, appreciate the present, and enjoy the tranquility of the evening.",
        "Good evening, sir! May your evening be a haven of peace, allowing you to unwind and recharge.",
        "Hello, sir! As the day gently turns into evening, may your surroundings be filled with calmness and comfort.",
        "Evening greetings, sir! Wishing you a serene and enjoyable evening as you wind down from the day.",
        "Good evening, sir! Reflect on the positive moments of the day as you embrace the tranquility of the evening.",
        "Hello, sir! As the sun sets, may your evening unfold with relaxation and moments of joy.",
        "Evening, sir! Take this opportunity to rejuvenate and prepare for a restful night ahead.",
        "Good evening, sir! Wishing you a serene and peaceful evening filled with positivity and happiness.",
        "Hello, sir! May your evening be a time of quiet reflection and enjoyment after a productive day.",
        "Evening greetings, sir! Take a break and soak in the peaceful ambiance of the evening hours.",
        "Good evening, sir! May the tranquility of the evening bring you moments of peace and contentment.",
        "Hello, sir! Wishing you a calm and relaxing evening as you unwind from the day's activities.",
        "Evening, sir! Take a moment to appreciate the beauty of the evening sky and the peace it brings.",
        "Good evening, sir! May your evening be filled with tranquility and moments of quiet joy.",
        "Hello, sir! As the day winds down, may your evening be a peaceful and enjoyable retreat.",
        "Evening greetings, sir! Take this time to rejuvenate and prepare for a restful night ahead.",
        "Good evening, sir! Wishing you a serene and joyful evening filled with positive moments.",
        "Hello, sir! As the sun sets, may your evening be as beautiful and tranquil as the changing sky.",
        "Evening, sir! Take a break and enjoy the simple pleasures that the evening has to offer.",
        "Good evening, sir! Reflect on the accomplishments of the day as you embrace the calmness of the evening.",
        "Hello, sir! Wishing you a delightful and peaceful evening as you unwind from the day's activities.",
        "Evening greetings, sir! Take this time to appreciate the beauty of the evening sky and the tranquility it brings.",
        "Good evening, sir! May your evening be filled with moments of peace, joy, and relaxation as you bid farewell to the day."
    ]
    selected_greeting = random.choice(good_evening_wish)
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(f"{selected_greeting}, it's {current_time}")
    speak(selected_greeting)
    speak(f"it's, {current_time}")
    Temp()
    rep()




def wish():
    if nowx.hour < 12:
        random_morning_greeting()
    elif nowx.hour < 16:
        random_afternoon_greeting()
    else:
        random_evening_greeting()


