import requests
from Body.speak import *

def get_current_location():
    try:
        # Get public IP address using ipify.org
        ip_add = requests.get('https://api.ipify.org').text.strip()
        print("Your public IP address:", ip_add)

        # Use the IP address to get location information from get.geojs.io
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_response = requests.get(url)
        geo_data = geo_response.json()

        # Extract city and country information from the response
        city = geo_data['city']
        country = geo_data['country']

        # Print or speak the location information
        print(f"You are currently in {city}, {country}.")
        speak(f"Sir, we are currently in {city} city, {country} country.")

    except Exception as e:
        print("Error:", e)
        speak("Sorry sir, I am unable to determine our current location due to a network issue.")

def getlocation():
    try:
        # Get public IP address using ipify.org
        ip_add = requests.get('https://api.ipify.org').text.strip()
        print("Your public IP address:", ip_add)

        # Use the IP address to get location information from get.geojs.io
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_response = requests.get(url)
        geo_data = geo_response.json()

        # Extract city and country information from the response
        city = geo_data['city']
        country = geo_data['country']

        # Print or speak the location information
        print(f"{city}, {country}.")

    except Exception as e:
        print("Error:", e)
        speak("Sorry sir, I am unable to determine our current location due to a network issue.")