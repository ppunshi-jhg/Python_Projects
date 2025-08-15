import requests
from typing import Final

BASE_URL:Final[str] = "https://api.coingecko.com/api/v3/coins/list"

def get_coins() -> list[dict]:
    payload: dict[str,str] = {"vs_currency": "aud", "order": "market_cap_desc"}
    
    response = requests.get(BASE_URL, params=payload)
    data = response.json()
    
    return [
        {
            "id": item["id"],
            "symbol": item["symbol"],
            "name": item["name"]
        }
        for item in data
    ]
    
if __name__ == "__main__":
    coins = get_coins()
    for coin in coins:
        print(f"{coin['name']} ({coin['symbol']}): {coin['id']}")
