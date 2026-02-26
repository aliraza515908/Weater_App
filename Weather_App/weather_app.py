# Weather App in Python (WeatherAPI)
# Author: Ali Raza
# Description: Fetches real-time weather using WeatherAPI

import requests

API_KEY = "fafe6e587ef04620a2b21615262602"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

def get_weather(city_name):
    city_name = city_name.strip()
    if not city_name:
        print("Please enter a valid city name.")
        return

    params = {
        "key": API_KEY,
        "q": city_name,
        "aqi": "no"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if "error" in data:
            print("City not found. Please check the city name.")
            return

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        print(f"\n🌍 Weather in {location}, {country}")
        print(f"🌡 Temperature: {temp}°C")
        print(f"☁ Condition: {condition}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind} km/h")

    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")

def main():
    print("🌤️  Welcome to the Python Weather App")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("Goodbye!")
            break
        get_weather(city)

if __name__ == "__main__":
    main()