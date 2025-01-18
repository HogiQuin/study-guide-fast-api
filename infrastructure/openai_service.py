from openai import OpenAI
from resources.en import TEXT_EN
from resources.es import TEXT_ES
from resources.fr import TEXT_FR
from resources.it import TEXT_IT
from resources.jp import TEXT_JP

class OpenAIService:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def get_response(self, topic: str, lang: str) -> str:
        print("Nos hablo data acces y nos solicito la informacion con el lenguaje:" + lang)
        if lang == "en":
            return str(TEXT_EN)
        if lang == "es":
            return str(TEXT_ES)
        if lang == "jp":
            return str(TEXT_JP)
        if lang == "fr":
            return str(TEXT_FR)
        if lang == "it":
            return str(TEXT_IT)
        
        return str({"text": "No data found for the specified language."})
        