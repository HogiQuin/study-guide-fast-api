class OpenInverstDataAccess:
    def __init__(self, open_inverst_service):
        self.open_inverst_service = open_inverst_service

    def fetch_symbol_inverst(self, symbol: str) -> str:
        print("recibimos request de business haremos el request a la infraestructura")
        
        inverst = self.open_inverst_service.get_inverst(symbol)
        print(inverst)
        return inverst