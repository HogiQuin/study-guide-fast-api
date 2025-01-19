import requests

class WeatherService:
    def __init__(self):
        self.api_key = "79772ccd8ded68d4ea9feb7165f77ecb"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str) -> str:
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'en'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()

            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            print("pase por infraestructura")
            return str(weather_info)
        except requests.exceptions.RequestException as e:
            return str({'error': str(e)})
        except KeyError:
            return str({'error': 'Invalid response from the API. Please check the city name or API key.'})