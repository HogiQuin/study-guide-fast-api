class OpenWeatherDataAccess:
    def __init__(self, open_weather_service):
        self.open_weather_service = open_weather_service

    def fetch_city_weather(self, city: str) -> str:
        print("recibimos request de business haremos el request a la infraestructura")
        
        weather = self.open_weather_service.get_weather(city)
        print(weather)
        return weather