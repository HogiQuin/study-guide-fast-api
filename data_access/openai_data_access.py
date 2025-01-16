class OpenAIDataAccess:
    def __init__(self, openai_service):
        self.openai_service = openai_service

    def fetch_response(self, topic: str, lang: str) -> str:
        return self.openai_service.get_response(topic, lang)