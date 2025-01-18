from fastapi import APIRouter, HTTPException
import os
from resources.greetings import GREETINGS

hello_router = APIRouter()

@hello_router.get("/world")
async def hello_world():
    try:
        print("Aqui entro al enrutador de hello world")
        return {"hello": "world"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@hello_router.get("/{name}")
async def hello_joseph(name: str, lang: str):
    try:
        print("Aqui entro al enrutador de joseph")
        print("ruta: / " + name)
        count_name = len(name)
        
        if lang == "en":
            if count_name <= 5:
                return str(name + ", " + GREETINGS["english"])
            else: 
                return str(GREETINGS["english"] + ", " + name)
        if lang == "jp":
            if count_name <= 5:
                return str(name + ", " + GREETINGS["japanese"])
            else: 
                return str(GREETINGS["japanese"] + ", " + name)
        if lang == "de":
            if count_name <= 5:
                return str(name + ", " + GREETINGS["detush"])
            else: 
                return str(GREETINGS["detush"] + ", " + name)
        if lang == "it":
            if count_name <= 5:
                return str(name + ", " + GREETINGS["italiano"])
            else: 
                return str(GREETINGS["italiano"] + ", " + name)
        

        return {"hello": name}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))