import os
import requests

def get_extension(url: str) -> str | None:
    extensions: list[str] = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    
    for ext in extensions:
        if ext in url:
            return ext
    return None

def download_image(url: str, name: str, folder: str = None):
    
    if ext:= get_extension(url):
        if folder:
            image_name = os.path.join(folder, f"{name}{ext}")
        else:
            image_name = f"{name}{ext}"
    
    else:
        raise Exception("Unsupported image format.")
    
    if os.path.exists(image_name):
        raise Exception(f"Image {image_name} already exists.")
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        with open(image_name, "wb") as file:
            file.write(response.content)
        
        print(f"Image downloaded successfully: {image_name}")
    except Exception as e:
        print(f"Failed to download image: {e}")
    
def main():
    url: str = input("Enter the image url: ")
    name: str = input("Enter the image name: ")
    
    print("Downloading image...")
    download_image(url, name, folder= "images")

if __name__ == "__main__":
    main()

