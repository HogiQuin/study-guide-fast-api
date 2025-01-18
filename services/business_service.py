class BusinessService:
    def __init__(self, data_access):
        self.data_access = data_access

    def generate_business_response(self, topic: str, lang: str) -> str:
        """
        Generates a business response by fetching data from the data access layer.

        Args:
            topic (str): The topic for which the response is to be generated.
            lang (str): The language in which the response is to be generated.

        Returns:
            str: The response fetched from the data access layer.
        """
        print("El enrutador nos mando al business y vamos a llamar al data acces")
        return self.data_access.fetch_response(topic, lang)