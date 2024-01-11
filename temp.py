
from Body.speak import speak  # Assuming you have the speak function implemented

import requests
import json


def get_temperature_openweathermap(city):
    api_key = "1be737aa91bc5e80430e62bea9db39a4"  # Replace with your actual OpenWeatherMap API key
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # send GET request to API endpoint
    response = requests.get(endpoint, params={"q": city, "appid": api_key, "units": "metric"})

    # check if the request was successful
    if response.status_code == 200:
        # parse JSON response
        data = json.loads(response.text)

        # check if 'main' key is present
        if 'main' in data:
            # extract temperature in Celsius
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            print("Error: 'main' key not found in API response")
    else:
        print(f"Error: Failed to fetch data from API. Status code: {response.status_code}")

    return None


def Temp():
    city = "Harohalli, Karnataka"

    # get temperature using OpenWeatherMap API
    temperature_celsius = get_temperature_openweathermap(city)

    if temperature_celsius is not None:
        print(f"The weather in {city} is {temperature_celsius}°C")
        speak(f"The weather in {city} is {temperature_celsius}°C")
    else:
        print("Temperature data not available.")


