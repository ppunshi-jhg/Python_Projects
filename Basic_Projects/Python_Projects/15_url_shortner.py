from typing import Final
import requests

API_KEY: Final[str] = "15f711f68133cb626891604e991e7a26"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"

def shorten_link(full_link: str) -> None:
    payload: dict = {"Key": API_KEY, "short": full_link}
    request = requests.get(BASE_URL, params = payload)
    data: dict = request.json()
    
    if url_data := data.get('url'):
        if url_data["status"] == 7:
            short_link: str = url_data["shortLink"]
            print("Link:", short_link)
        else:
            print("Error status:", url_data["status"])
    
def main() -> None:
    link: str = input("Enter a link to shorten: ")
    shorten_link(link)

if __name__ == "__main__":
    main()