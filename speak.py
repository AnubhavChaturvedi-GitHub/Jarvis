import sys
import threading
import  time
import pyttsx3
from textblob import TextBlob

def detect_emotion(text):
    text_lower = text.lower()

    # Keywords for different feelings
    ecstatic_keywords = ['ecstatic']
    overjoyed_keywords = ['overjoyed']
    elated_keywords = ['elated']
    joyful_keywords = ['joyful']
    happy_keywords = ['happy']
    cheerful_keywords = ['cheerful']
    content_keywords = ['content']
    pleased_keywords = ['pleased']
    neutral_keywords = ['neutral']
    indifferent_keywords = ['indifferent']
    unhappy_keywords = ['unhappy']
    sad_keywords = ['sad']
    mournful_keywords = ['mournful']
    despondent_keywords = ['despondent']
    melancholy_keywords = ['melancholy']
    depressed_keywords = ['depressed']
    devastated_keywords = ['devastated']
    hopeful_keywords = ['hopeful']
    optimistic_keywords = ['optimistic']
    grateful_keywords = ['grateful']
    inspired_keywords = ['inspired']
    amused_keywords = ['amused']
    calm_keywords = ['calm']
    confused_keywords = ['confused']
    disappointed_keywords = ['disappointed']
    frustrated_keywords = ['frustrated']
    anxious_keywords = ['anxious']
    overwhelmed_keywords = ['overwhelmed']
    guilty_keywords = ['guilty']
    disgusted_keywords = ['disgusted']
    repulsed_keywords = ['repulsed']
    detached_keywords = ['detached']

    # Check for each emotion
    if any(word in text_lower for word in ecstatic_keywords):
        return "ecstatic"
    elif any(word in text_lower for word in overjoyed_keywords):
        return "overjoyed"
    elif any(word in text_lower for word in elated_keywords):
        return "elated"
    elif any(word in text_lower for word in joyful_keywords):
        return "joyful"
    elif any(word in text_lower for word in happy_keywords):
        return "happy"
    elif any(word in text_lower for word in cheerful_keywords):
        return "cheerful"
    elif any(word in text_lower for word in content_keywords):
        return "content"
    elif any(word in text_lower for word in pleased_keywords):
        return "pleased"
    elif any(word in text_lower for word in neutral_keywords):
        return "neutral"
    elif any(word in text_lower for word in indifferent_keywords):
        return "indifferent"
    elif any(word in text_lower for word in unhappy_keywords):
        return "unhappy"
    elif any(word in text_lower for word in sad_keywords):
        return "sad"
    elif any(word in text_lower for word in mournful_keywords):
        return "mournful"
    elif any(word in text_lower for word in despondent_keywords):
        return "despondent"
    elif any(word in text_lower for word in melancholy_keywords):
        return "melancholy"
    elif any(word in text_lower for word in depressed_keywords):
        return "depressed"
    elif any(word in text_lower for word in devastated_keywords):
        return "devastated"
    elif any(word in text_lower for word in hopeful_keywords):
        return "hopeful"
    elif any(word in text_lower for word in optimistic_keywords):
        return "optimistic"
    elif any(word in text_lower for word in grateful_keywords):
        return "grateful"
    elif any(word in text_lower for word in inspired_keywords):
        return "inspired"
    elif any(word in text_lower for word in amused_keywords):
        return "amused"
    elif any(word in text_lower for word in calm_keywords):
        return "calm"
    elif any(word in text_lower for word in confused_keywords):
        return "confused"
    elif any(word in text_lower for word in disappointed_keywords):
        return "disappointed"
    elif any(word in text_lower for word in frustrated_keywords):
        return "frustrated"
    elif any(word in text_lower for word in anxious_keywords):
        return "anxious"
    elif any(word in text_lower for word in overwhelmed_keywords):
        return "overwhelmed"
    elif any(word in text_lower for word in guilty_keywords):
        return "guilty"
    elif any(word in text_lower for word in disgusted_keywords):
        return "disgusted"
    elif any(word in text_lower for word in repulsed_keywords):
        return "repulsed"
    elif any(word in text_lower for word in detached_keywords):
        return "detached"

    # If none of the emotions are detected
    return "unknown"

def get_emotion(sentiment):
    if sentiment > 0.7:
        return "ecstatic", (220, 1.5)
    elif 0.6 <= sentiment <= 0.7:
        return "overjoyed", (180, 1.4)
    elif 0.5 <= sentiment < 0.6:
        return "elated", (190, 1.3)
    elif 0.5 <= sentiment < 0.6:
        return "angry", (290, 1.3)
    elif 0.4 <= sentiment < 0.5:
        return "joyful", (180, 1.2)
    elif 0.3 <= sentiment < 0.4:
        return "happy", (170, 1.1)
    elif 0.2 <= sentiment < 0.3:
        return "cheerful", (160, 1.0)
    elif 0.1 <= sentiment < 0.2:
        return "content", (150, 0.9)
    elif 0.05 <= sentiment < 0.1:
        return "pleased", (140, 0.8)
    elif -0.05 <= sentiment < 0.05:
        return "neutral", (130, 1)
    elif -0.1 <= sentiment < -0.05:
        return "indifferent", (120, 1)
    elif -0.2 <= sentiment < -0.1:
        return "unhappy", (110, 1)
    elif -0.3 <= sentiment < -0.2:
        return "sad", (100, 1)
    elif -0.4 <= sentiment < -0.3:
        return "mournful", (100, 1)
    elif -0.5 <= sentiment < -0.4:
        return "despondent", (170, 1)
    elif -0.6 <= sentiment < -0.5:
        return "melancholy", (170, 0.1)
    elif -0.7 <= sentiment < -0.6:
        return "depressed", (60, 1)
    elif sentiment <= -0.7:
        return "devastated", (180, 1)
    elif 0.5 <= sentiment < 0.6:
        return "hopeful", (175, 1.3)
    elif 0.4 <= sentiment < 0.5:
        return "optimistic", (165, 1.2)
    elif 0.3 <= sentiment < 0.4:
        return "grateful", (155, 1.1)
    elif 0.2 <= sentiment < 0.3:
        return "inspired", (145, 1.0)
    elif 0.1 <= sentiment < 0.2:
        return "amused", (135, 0.9)
    elif 0.05 <= sentiment < 0.1:
        return "calm", (125, 0.8)
    elif -0.05 <= sentiment < 0.05:
        return "confused", (115, 0.8)
    elif -0.1 <= sentiment < -0.05:
        return "disappointed", (105, 0.9)
    elif -0.2 <= sentiment < -0.1:
        return "frustrated", (100, 0.5)
    elif -0.3 <= sentiment < -0.2:
        return "anxious", (85, 0.8)
    elif -0.4 <= sentiment < -0.3:
        return "overwhelmed", (100, 1)
    elif -0.5 <= sentiment < -0.4:
        return "guilty", (100, 1)
    elif -0.6 <= sentiment < -0.5:
        return "disgusted", (100, 1)
    elif -0.7 <= sentiment < -0.6:
        return "repulsed", (100, 1)
    elif sentiment <= -0.7:
        return "detached", (150, 0.8)

    # Add more emotions as needed

def track_emotion_phrases(text):
    if any(word in text.lower() for word in ['Love', 'Romance', 'Affection', 'Passion', 'Adoration', 'Devotion', 'Intimacy', 'Fondness', 'Tenderness', 'Caring',
 'Warmth', 'Amour', 'Infatuation', 'Desire', 'Attraction', 'Yearning', 'Admiration', 'Enchantment', 'Sweetheart', 'Soulmate',
 'Heartfelt', 'Tender', 'Embrace', 'Cherish', 'Butterfly', 'Sweetness', 'Amorous', 'Sentiment', 'Woo', 'Serenade', 'Passionate',
 'Hug', 'Kiss', 'Whisper', 'Yearn', 'Lovers', 'Connection', 'Affinity', 'Magnetic', 'Attracted', 'Romance', 'Cupid', 'Tenderhearted',
 'Beloved', 'Emotion', 'Fond', 'Harmony', 'Sympathy', 'Infatuated', 'Enamored', 'Darling', 'Tenderly', 'Suitor', 'Enraptured',
 'Heartwarming', 'Softness', 'Heartthrob', 'Amicable', 'Attachment', 'Honeyed', 'Admirer', 'Yearning', 'Adorned', 'Passionflower',
 'Swoon', 'Entranced', 'Enveloped', 'Heartfelt', 'Heartstrings', 'Enamored', 'Lovestruck', 'Warmhearted', 'Adulating',
 'Companionate', 'Quixotic', 'Wooing', 'Nurturing', 'Stargazing', 'Whispers', 'Harmony', 'Languishing', 'Enthralled',
 'Romeo', 'Juliet', 'Emblazoned', 'Fancy', 'Allure', 'Rapture', 'Yearning', 'Enraptured', 'Yearning', 'Fantasy', 'Intoxication',
 'Longing', 'Alluring', 'Savor', 'Spark', 'Enchanted', 'Longing', 'Elation']
):
        return "love"
    elif any(word in text.lower() for word in ['Happy', 'Joyful', 'Pleased', 'Content', 'Cheerful', 'Delighted', 'Elated', 'Exuberant', 'Jovial', 'Blissful',
'Euphoric', 'Merry', 'Upbeat', 'Radiant', 'Sunny', 'Ecstatic', 'Buoyant', 'Lighthearted', 'Vibrant', 'Carefree',
 'Satisfied', 'Optimistic', 'Whimsical', 'Playful', 'Jubilant', 'Grateful', 'Spirited', 'Enthusiastic', 'Exhilarated',
 'Blessed', 'Mirthful', 'Gleeful', 'Hopeful', 'Sunny', 'Peppy', 'Zestful', 'Jocular', 'Sprightly', 'Jolly', 'Animated',
 'Elfin', 'Satisfied', 'Blithe', 'Pleasurable', 'Radiant', 'Chipper', 'Jaunty', 'Chirpy', 'Upbeat', 'Zippy']
):
        return "happy"
    elif any(word in text.lower() for word in ['Peaceful', 'Serene', 'Tranquil', 'Calm', 'Content', 'Satisfied', 'Pleased', 'Fulfilled', 'Blissful', 'Harmonious',
 'Relaxed', 'At ease', 'Reassured', 'Placid', 'Soothed', 'Undisturbed', 'Gratified', 'Composed', 'Assured', 'Tranquility',
 'Repose', 'Comforted', 'Untroubled', 'Quieted', 'Restful', 'Eased', 'At peace', 'Serenity', 'Easeful', 'Balanced',
 'Steady', 'Hushed', 'Calmness', 'Heartsease', 'Pacified', 'Undisturbed', 'Placid', 'Halcyon', 'Pacification', 'At rest',
 'Replenished', 'Mild', 'Equanimity', 'Centred', 'Unperturbed', 'Contentedness', 'Contentment', 'Satisfaction', 'Ease']
):
        return "content"
    elif any(word in text.lower() for word in ['Neutral', 'Indifferent', 'Calm', 'Composed', 'Unaffected', 'Impartial', 'Detached', 'Unbiased', 'Unemotional',
 'Dispassionate', 'Objective', 'Uninvolved', 'Unperturbed', 'Unresponsive', 'Stoic', 'Imperturbable', 'Nonchalant',
 'Aloof', 'Distant', 'Equanimous', 'Balanced', 'Unflappable', 'Cool-headed', 'Serene', 'Tranquil', 'Noncommittal',
 'Unfazed', 'Undisturbed', 'Unruffled', 'Untroubled', 'Easygoing', 'Unconcerned', 'Unexcitable', 'Unmoved', 'Unfeeling',
 'Remote', 'Impassive', 'Unimpressed', 'Unworried', 'Nonplussed', 'Matter-of-fact', 'Unresponsive', 'Cool', 'Reserved',
 'Untouched', 'Unbiased', 'Detached', 'Unprejudiced', 'Disinterested', 'Unbiased']
):
        return "neutral"
    elif any(word in text.lower() for word in ['Moody', 'Unsettled', 'Irritable', 'Restless', 'Discontent', 'Grumpy', 'Crabby', 'Testy', 'Peevish', 'Gloomy',
 'Sullen', 'Sulky', 'Brooding', 'Fretful', 'Edgy', 'Perturbed', 'Tense', 'Restive', 'Anxious', 'Agitated', 'Nervous',
 'Uneasy', 'Pouty', 'Choleric', 'Querulous', 'Cranky', 'Cross', 'Pensive', 'Melancholy', 'Blue', 'Mournful', 'Downcast',
 'Glum', 'Lamenting', 'Wistful', 'Yearning', 'Displeased', 'Dissatisfied', 'Malcontent', 'Grumbling', 'Craving',
 'Whining', 'Frowning', 'Dejected', 'Depressed', 'Dismal', 'Despondent', 'Downhearted', 'Worried', 'Aggrieved', 'Miffed']
):
        return "moody"
    elif any(word in text.lower() for word in ['Sad', 'Unhappy', 'Mournful', 'Disheartened', 'Dejected', 'Downcast', 'Downhearted', 'Melancholy', 'Blue', 'Sorrowful',
 'Depressed', 'Dismal', 'Despondent', 'Forlorn', 'Gloomy', 'Dreary', 'Woeful', 'Cheerless', 'Heartbroken', 'Desolate',
 'Somber', 'Down in the dumps', 'Downhearted', 'Low-spirited', 'Downcast', 'Inconsolable', 'Miserable', 'Glum', 'Morose',
 'Sullen', 'Wretched', 'Regretful', 'Lamenting', 'Grief-stricken', 'Long-faced', 'Woebegone', 'Doleful', 'Heartrending',
 'Tearful', 'Funereal', 'Tragic', 'Mournful', 'Lachrymose', 'Weepy', 'Morbid', 'Anguished', 'Heavyhearted', 'Sulky', 'Pensive']
):
        return "sad"
    elif any(word in text.lower() for word in ['Angry', 'Irate', 'Furious', 'Enraged', 'Agitated', 'Irritated', 'Infuriated', 'Incensed', 'Raging', 'Indignant',
 'Wrathful', 'Livid', 'Maddened', 'Exasperated', 'Annoyed', 'Provoked', 'Irked', 'Fuming', 'Outraged', 'Hostile',
 'Fierce', 'Resentful', 'Tempestuous', 'Stormy', 'Choleric', 'Vexed', 'Bitter', 'Offended', 'Cross', 'Huffy', 'Riled',
 'Upset', 'Tumultuous', 'Spiteful', 'Sullen', 'Rancorous', 'Sour', 'Irritable', 'Testy', 'Petulant', 'Peevish',
 'Incensed', 'Infuriated', 'Inflamed', 'Burning', 'Hot-tempered', 'Out of control', 'Wrath', 'Hostility', 'Vehement']
):
        return "angry"

    else:
        return None

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.050)  # Adjust the sleep duration for the animation speed
    print()
def speakbasic(text):
    try:
        rate = 300
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)

        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        emotion, (adjusted_rate, adjusted_volume) = get_emotion(sentiment)

        tracked_emotion = track_emotion_phrases(text)

        if tracked_emotion: emotion = tracked_emotion

        # Adjust speech characteristics based on emotion
        engine.setProperty('rate', adjusted_rate)
        engine.setProperty('volume', adjusted_volume)

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Error: {e}")

def speak(text):
    speak_thread = threading.Thread(target=speakbasic, args=(text,))
    speak_thread.start()

    # Thread for printing with animation
    print_thread = threading.Thread(target=print_animated_message, args=(f"J.A.R.V.I.S : {text}",))
    print_thread.start()

    # Wait for both threads to finish
    speak_thread.join()
    print_thread.join()

