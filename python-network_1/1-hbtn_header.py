import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    respond = requests.get(url)
    result = respond.headers.get('X-Request-Id')
    print(result)
