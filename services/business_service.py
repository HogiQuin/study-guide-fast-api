class BusinessService:
    def __init__(self, data_access):
        self.data_access = data_access

    def generate_business_response(self, topic: str, lang: str) -> str:
        print("el enrutador nos mando al business y vamos a mandar llamar al data access")
        return self.data_access.fetch_response(topic, lang)