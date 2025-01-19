from data_access.open_weather_data_access import OpenWeatherDataAccess
from fastapi import APIRouter, HTTPException
from infrastructure.open_weather_service import WeatherService
from services.open_weather_bll import OpenWeatherBLL

weather_router = APIRouter()

open_weather_service = WeatherService()
open_weather_data_access = OpenWeatherDataAccess(open_weather_service=open_weather_service)
open_weather_bll = OpenWeatherBLL(open_weather_data_access=open_weather_data_access)
  
@weather_router.get("/{city}")
async def open_weather(city: str):
    try:
        print("aqui entro al enrutador de open_weather")
        print("ruta: /" + city)

        return open_weather_bll.get_city_weather(city)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))