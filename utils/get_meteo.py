import requests
import json
from datetime import datetime, timedelta

# Load the configuration
with open('config/config.json', 'r') as config_file:
    config = json.load(config_file)
    
API_KEY = config['apis'].get('OpenWeatherMap')
cities = config.get('cities', [])

def get_actual_date():
    return datetime.now().strftime('%Y-%m-%d')

def get_tomorrow_date():
    tomorrow = datetime.now() + timedelta(1)
    return tomorrow.strftime('%Y-%m-%d')

def get_city_coordinates(city: str, api_key: str):
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    try:
        response = requests.get(base_url, params={
            'q': city,
            'limit': 5,
            'appid': api_key
        })
        data = response.json()
        
        if response.status_code == 200 and data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            return lat, lon
        else:
            return None
    except Exception as e:
        print(f"Error getting coordinates for {city}: {str(e)}")
        return None
    
def get_weather(city: str):
    try:
        lat, lon = get_city_coordinates(city, API_KEY)
        print(f'{city}:   {lat}  {lon}')
        BASE_URL = 'http://api.openweathermap.org/data/3.0/onecall'
        response = requests.get(BASE_URL, params={
            'lat': lat,
            'lon': lon,
            'exclide': 'hourly,minutely,current',
            'units': 'metric',
            'lang': 'fr',
            'appid': API_KEY
        })
        data = response.json()
        tomorrow_weather = data['daily'][1]
        print(tomorrow_weather)
        
        if response.status_code == 200:
            weather = {
                'city': city,
                'temperature': tomorrow_weather['temp'],
                'temperature_feels_like': tomorrow_weather['feels_like'],
                'summary': tomorrow_weather['summary'],
                'description': tomorrow_weather['weather'][0]['description'],
                'humidity': tomorrow_weather['humidity'],
                'wind_speed': tomorrow_weather['wind_speed']
            }
            return weather
        else:
            print("ERROR: ", data)
            return {'city': city, 'error': data.get('message', 'Unknown error')}
    except Exception as e:
        return {'city': city, 'error': str(e)}

def get_weather_all_cities():
    weather_data = []
    for city in cities:
        weather = get_weather(city)
        weather_data.append(weather)
        
    return weather_data


if __name__ == '__main__':
    print(get_weather_all_cities())
