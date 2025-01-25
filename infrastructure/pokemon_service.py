import requests

class PokemonService:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon(self, pokemon):
        response = requests.get(f"{self.base_url}/{pokemon}")

        if response.status_code != 200:
            return {"error": f"HTTP error: {response.status_code}"}

        data = response.json()

        return str(data)