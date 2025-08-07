import requests

def check_url(url):
    url = url.strip()
    
    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url
    elif url.startswith("http://"):
        url = "https://" + url[len("http://"):]
    return url

def website_checker(urls):
    results = []
    
    urls = urls.split(",")
    urls = [url.strip() for url in urls if url.strip()]
    
    for url in urls:
        url = check_url(url)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results.append(f"{url} is reachable.")
            elif response.status_code == 404:
                results.append(f"{url} is not found (404). ")
            elif response.status_code == 403:
                results.append(f"{url} is forbidden (403). ")
            else:
                results.append(f"{url} returned status code {response.status_code}.")
        except requests.exceptions.RequestException as e:
            results.append(f"Error checking {url}: {e}")
            
    return results

if __name__ == "__main__":
    urls = input("Enter URLs separated by commas: ")
    results = website_checker(urls)
    for result in results:
        print(result)
        
    