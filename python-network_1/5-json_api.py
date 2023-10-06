import requests
import sys

def search(letter):
    url = "http://0.0.0.0:5000/search_user"
    params = {'q': letter}
    response = requests.post(url, params=params)

    try:
        response.raise_for_status()
        user_data = response.json()
        if user_data:
            print(f"[{user_data['id']}] {user_data['name']}")
        else:
            print("No result")
    except (requests.exceptions.HTTPError, ValueError):
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search(letter)
