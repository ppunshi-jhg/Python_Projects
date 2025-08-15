import requests
from dataclasses import dataclass
from typing import Final

BASE_URL: Final[str] = "https://api.coingecko.com/api/v3/coins/list"

@dataclass
class Coin:
    id: str
    symbol: str
    name: str
    

def get_coins() -> list[Coin]:
    """Fetch the list of cryptocurrencies from CoinGecko."""
    payload: dict[str,str] = {"vs_currency": "aud", "order": "market_cap_desc"}
    response = requests.get(BASE_URL, params = payload)
    data = response.json()
    
    coin_list: list[Coin] = []
    for item in data:
        coin: Coin = Coin(
            id = item['id'],
            symbol = item['symbol'],
            name = item['name']
        )
        
        coin_list.append(coin)
    
    return coin_list

if __name__ == "__main__":
    coins = get_coins()
    for coin in coins:
        print(f"{coin.name} ({coin.symbol}): {coin.id}")