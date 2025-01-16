class BusinessService:
    def __init__(self, data_access):
        self.data_access = data_access

    def generate_business_response(self, topic: str, lang: str) -> str:
        return self.data_access.fetch_response(topic, lang)