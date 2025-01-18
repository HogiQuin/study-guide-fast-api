from fastapi import APIRouter, HTTPException
from resources.greetings import GREETINGS

hello_router = APIRouter()

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
                return str(name + ", " + GREETINGS["german"])
            else: 
                return str(GREETINGS["german"] + ", " + name)
        if lang == "it":
            if count_name <= 5: 
                return str(name + ", " + GREETINGS["italian"])
            else: 
                return str(GREETINGS["italian"] + ", " + name)
    
        return {"hello": name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))