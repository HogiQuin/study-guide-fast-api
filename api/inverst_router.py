from data_access.inverst_data_access import InvertsDataAccess
from fastapi import APIRouter, HTTPException
from infrastructure.inverst_info_service import AlphaVantageClient
from services.inverst_bll import InverstBLL


inverst_router = APIRouter()


inverst_info_service = AlphaVantageClient()
inverst_data_access = InvertsDataAccess(inverst_info_service=inverst_info_service)
inverst_bll = InverstBLL(inverst_data_access=inverst_data_access)
  

#normalmente aqui todo es mas sencuillo, pero como se esta haciendo una inyeccion de dependencias, se tiene que hacer de esta manera
#me gusta por que inicio comentando algo y copilot anda al tiro con el codigo, completa mis comentarios, pero me gusta


async def inverst(inverst_id: str):
    try:
        print("aqui entro al enrutador de inverst")
        return inverst_bll.get_inverst_info(inverst_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#son las 4 de la mañana y no se me ocurre que mas poner, pero aqui ando todavia