import requests
from Body.speak import *

def get_weather():
    api_key = '1be737aa91bc5e80430e62bea9db39a4'

    # Replace 'CITY_NAME' with the name of the city you want to check the weather for
    city = 'Harohalli, Karnataka'
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def check_cloud_cover(weather_data):
    if weather_data:
        try:
            clouds = weather_data['clouds']['all']
            print(f"Cloud coverage Condition : {clouds}%")
            speak(f"Cloud coverage Condition : {clouds}%")

            # Check if weather description is available
            if 'weather' in weather_data and weather_data['weather']:
                weather_description = weather_data['weather'][0]['description']
                print(f"I believes today, {weather_description} ,Can easily visible in the sky")
                speak(f"I believes today, {weather_description} ,Can easily visible in the sky")

            # Check if rain information is available
            if 'rain' in weather_data and '1h' in weather_data['rain']:
                rain_amount = weather_data['rain']['1h']
                print(f"Rain in the last hour: {rain_amount} mm")
                speak(f"Rain in the last hour: {rain_amount} mm")

                # Check if rain prediction is available
                if 'rain' in weather_data and '3h' in weather_data['rain']:
                    rain_prediction = weather_data['rain']['3h']
                    print(f"Rain prediction for the next 3 hours: {rain_prediction} mm")
                    speak(f"Rain prediction for the next 3 hours: {rain_prediction} mm")

            # Check if snow information is available
            if 'snow' in weather_data and '1h' in weather_data['snow']:
                snow_amount = weather_data['snow']['1h']
                print(f"Snow in the last hour: {snow_amount} mm")

        except KeyError:
            print("Some weather information not available.")
    else:
        print("Failed to retrieve weather information.")



def rep():
    weather_data = get_weather()
    check_cloud_cover(weather_data)


