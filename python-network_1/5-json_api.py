import requests
import sys
if __name__ == "__main__":
    newData = {
        "letter": "q"
    }
    url_post = "http://0.0.0.0:5000/search_user"
    post_response = requests.post(url_post, json=newData)
    # Print the response
    if post_response is None:
        print("Not a valid JSON")
    elif not post_response:
        print("No result")
    else:
        print("[{}] {}".format(post_response['id'], post_response['name']))
    