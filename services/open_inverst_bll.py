class OpenInverstBLL:
    def __init__(self, open_inverst_data_access):
        self.open_inverst_data_access = open_inverst_data_access

    def get_symbol_inverst(self, symbol: str) -> str:
        print("el enrutador nos mando al business y vamos a mandar llamar al data access")
        inverst = self.open_inverst_data_access.fetch_symbol_inverst(symbol)
        return inverst
