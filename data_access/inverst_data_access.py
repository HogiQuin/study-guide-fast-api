class InvertsDataAccess:
    def __init__(self, inverst_info_service):
        self.inverst_info_service = inverst_info_service

    def fetch_inverst_info(self, inverst_id: str) -> str:
        print("recibimos request de business haremos el request a la infraestructura")
        
        inverst_info = self.inverst_info_service.get_inverst_info(inverst_id)
        print(inverst_info)
        return inverst_info
    
