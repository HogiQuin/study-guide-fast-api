
from resources.greetings import GREETINGS


class GreetingService:
    def __init__(self):
        pass

    def get_greeting(self, lang: str) -> str:
        print("nos hablo data access y nos solicito informacion con el lenguaje: " + lang)
       
        return str(GREETINGS[lang])
    