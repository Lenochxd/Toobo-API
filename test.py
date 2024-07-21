import requests
from datetime import datetime, timedelta

# Replace with your actual OpenWeatherMap API key
API_KEY = '703a94908c0a873cbd9e5bdf45e5a4bd'

# Specify the city and country
city = 'Paris'
country = 'FR'

# Construct the API URL for the current weather to get latitude and longitude
current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}&units=metric"

# Fetch the current weather data
response = requests.get(current_weather_url)

# Check for errors in the response
if response.status_code != 200:
    print(f"Error fetching current weather data: {response.json()}")
else:
    data = response.json()

    # Extract the latitude and longitude
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']

    # Construct the API URL for the 7-day forecast
    forecast_url = f"http://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=hourly,minutely,current&appid={API_KEY}&units=metric"

    # Fetch the forecast data
    response = requests.get(forecast_url)

    # Check for errors in the response
    if response.status_code != 200:
        print(f"Error fetching forecast data: {response.json()}")
    else:
        forecast_data = response.json()

        # Calculate the index for tomorrow's weather
        tomorrow_index = 1
        tomorrow_weather = forecast_data['daily'][tomorrow_index]

        # Extract relevant information
        temp_day = tomorrow_weather['temp']['day']
        weather_description = tomorrow_weather['weather'][0]['description']
        date_tomorrow = datetime.now() + timedelta(days=1)

        # Print the results
        print(f"Weather for tomorrow ({date_tomorrow.strftime('%Y-%m-%d')}) in {city}:")
        print(f"Temperature: {temp_day}°C")
        print(f"Description: {weather_description.capitalize()}")
