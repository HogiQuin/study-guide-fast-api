class GreetingDataAccess:
    def __init__(self, greeting_service):
        self.greeting_service = greeting_service

    def fetch_greeting(self, lang: str) -> str:
        print("recibimos request de business haremos el request a la infraestructura")
        config_map = {
            "en": "english",
            "it": "italian",
            "jp": "japanese",
            "de": "german"
        }
        return self.greeting_service.get_greeting(config_map[lang])