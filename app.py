from fastapi import FastAPI
from api.routers import router
from api.hello_router import hello_router
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()
app.include_router(router, prefix="/api")
app.include_router(hello_router, prefix="/hello")