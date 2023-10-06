import sys
import requests
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    jsonobj = response.json()
    print(jsonobj.get(id))
