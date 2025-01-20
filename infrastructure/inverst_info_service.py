import requests

class AlphaVantageClient:
    def __init__(self):
        self.api_key = "OLUAWJ9D7OWPLP9T"
        self.base_url = "https://www.alphavantage.co/query"

    def get_inverst_info(self, symbol):
        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": self.api_key,
            "outputsize": "compact"
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            return {"error": f"HTTP error: {response.status_code}"}

        data = response.json()

        try:
            time_series = data["Time Series (Daily)"]
            latest_date = max(time_series.keys())
            latest_data = time_series[latest_date]

            return str({
                "Date": latest_date,
                "Open": latest_data["1. open"],
                "High": latest_data["2. high"],
                "Low": latest_data["3. low"],
                "Close": latest_data["4. close"]
            })
        except KeyError:
            return str({"error": "Invalid or unexpected data format from API"})
        IBM, AAPL