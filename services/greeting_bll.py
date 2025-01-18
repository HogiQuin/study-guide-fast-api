class GreetingBLL:
    def __init__(self, greeting_data_access):
        self.greeting_data_access = greeting_data_access

    def generate_greeting_response(self, name: str, lang: str) -> str:
        print("el enrutador nos mando al business y vamos a mandar llamar al data access")
        greeting = self.greeting_data_access.fetch_greeting(lang)
        count_name = len(name)

        if count_name <= 5:
            return name + ", " + greeting
        else:
            return greeting + ", " + name