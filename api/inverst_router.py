from data_access.open_inverst_data_access import OpenInverstDataAccess
from fastapi import APIRouter, HTTPException
from infrastructure.open_inverst_service import AlphaVantageClient
from services.open_inverst_bll import OpenInverstBLL

inverst_router = APIRouter()

open_inverst_service = AlphaVantageClient()
open_inverst_data_access = OpenInverstDataAccess(open_inverst_service=open_inverst_service)
open_inverst_bll = OpenInverstBLL(open_inverst_data_access=open_inverst_data_access)
  
@inverst_router.get("/{symbol}")
async def open_inverst(symbol: str):
    try:
        print("aqui entro al enrutador de open_inverst")
        print("ruta: /" + symbol)

        return open_inverst_bll.get_symbol_inverst(symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

