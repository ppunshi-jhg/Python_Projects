from typing import Final
import requests
import json

#Constants
BASE_URL: Final[str] = "http://api.exchangeratesapi.io/v1/latest"
API_KEY: Final[str] = "6a1dfab98377aa87daca27148912b12d"

def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('C:\\Users\\arora\\OneDrive - John Holland Group\\Github Repos\\Python Projects\\Basic_Projects\\Python_Projects\\Currency_Converter\\rates.json', 'r') as file:
            return json.load(file)
    
    payload: dict[str] = {'access_key': API_KEY}
    request = requests.get(BASE_URL, params = payload)
    data:dict = request.json()
    
    # with open('rates.json', 'w') as file:
    #     json.dump(data, file)
    #I have commented out the above code after making the json file in the first go, once we have the json file then we dont need this code
        
    return data

def get_currency(currency: str, rates: dict) -> float:
    currency = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f"Currency {currency} not found")
    
def convert_currency(amount: float, from_currency: str, to_currency: str, rates:dict) -> float:
    from_rate = get_currency(from_currency, rates)
    to_rate = get_currency(to_currency, rates)
    print(f"The converted amount is from {amount} {from_currency} to {amount /from_rate * to_rate:,.2f} {to_currency}")


def main():
    data: dict = get_rates(mock = True)
    rates: dict = data.get('rates')
    
    convert_currency(100, "USD", "EUR", rates)
    
if __name__ == '__main__':
    main()
