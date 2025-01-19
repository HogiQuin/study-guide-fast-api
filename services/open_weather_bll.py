class OpenWeatherBLL:
    def __init__(self, open_weather_data_access):
        self.open_weather_data_access = open_weather_data_access

    def get_city_weather(self, city: str) -> str:
        print("el enrutador nos mando al business y vamos a mandar llamar al data access")
        weather = self.open_weather_data_access.fetch_city_weather(city)
        return weather
