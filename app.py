from fastapi import FastAPI
from api.routers import router
from api.hello_router import hello_router
from api.weather_router import weather_router
from api.inverst_router import inverst_router
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()
app.include_router(router, prefix="/api")
app.include_router(hello_router, prefix="/hello")
app.include_router(weather_router, prefix="/weather")
app.include_router(inverst_router, prefix="/inverst")