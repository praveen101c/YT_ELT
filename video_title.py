import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
user_input = input("Enter your Search: ")

def title_name():
    try:
        url = f"https://ww.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={user_input}&key={API_KEY}"
        response = requests.get(url)

        # Check response content
        print("Status code:", response.status_code)

        response.raise_for_status()
        data = response.json()

        print(json.dumps(data, indent=4))  # pretty print

        title_name = data['items'][0]['snippet']['title']
        print("title_name : ", title_name)
        return title_name
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None
    except (KeyError, IndexError):
        print("No items found in response")
        return None

if __name__ == "__main__":
    print(title_name())
