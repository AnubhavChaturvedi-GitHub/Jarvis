import requests
from Body.speak import speak
import sys
import time
import threading

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)  # Adjust the sleep duration for the animation speed
    print()
def get_news(api_key):
    api_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")


def display_top_news(news_data):
    if 'articles' in news_data:
        articles = news_data['articles'][:5]  # Get the top 5 articles
        for i, article in enumerate(articles, start=1):
            title = article.get('title', 'N/A')
            ans = f"{i}. {title}"

            animate_thread = threading.Thread(target=print_animated_message, args=(ans,))
            # Create a thread for speaking the message
            speak_thread = threading.Thread(target=speak, args=(ans,))

            # Start both threads concurrently
            animate_thread.start()
            speak_thread.start()

            # Wait for both threads to finish
            animate_thread.join()
            speak_thread.join()
    else:
        print("Unable to fetch news.")


def news():
    api_key = '680a13abaeb14d3f9dd4009e4f18a68c'  # Replace 'YOUR_API_KEY' with your actual API key from newsapi.org

    news_data = get_news(api_key)

    if news_data:
        print("\nTop 5 News Headlines for Today:\n")
        display_top_news(news_data)

