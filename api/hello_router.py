from data_access.greeting_data_access import GreetingDataAccess
from fastapi import APIRouter, HTTPException
from infrastructure.greetings_service import GreetingService
from resources.greetings import GREETINGS
from services.greeting_bll import GreetingBLL

hello_router = APIRouter()

greeting_service = GreetingService()
greeting_data_access = GreetingDataAccess(greeting_service=greeting_service)
greeting_bll = GreetingBLL(greeting_data_access=greeting_data_access)

@hello_router.get("/world")
async def hello_world():
    try:
        print("aqui entro al enrutador de heelo_world")
        print("ruta: /world")
        return {"hello": "world"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
  
@hello_router.get("/{name}")
async def hello_mady(name: str, lang: str):
    try:
        print("aqui entro al enrutador de heelo_world")
        print("ruta: /" + name)

        return greeting_bll.generate_greeting_response(name, lang)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))