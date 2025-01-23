class InverstBLL:
    def __init__(self, inverst_data_access):
        self.inverst_data_access = inverst_data_access

    def get_inverst_info(self, inverst_id: str) -> str:
        # El enrutador nos mandó al business y vamos a mandar llamar al data access
        print("el enrutador nos mando al business y vamos a mandar llamar al data access")
        inverst = self.inverst_data_access.fetch_inverst_info(inverst_id)
        return inverst
#ojo al inverst id, es el id de la inversion, no el id del usuario y bueno el fetch inverst info es el que se encarga de hacer la peticion a la infraestructura
     