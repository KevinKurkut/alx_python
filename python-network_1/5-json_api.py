import requests
import sys
if __name__ == "__main__":
    if len(sys.argv)>1:
        q=sys.argv[1]
    else:
        q=""
    url_post = "http://0.0.0.0:5000/search_user"    
    newData={"q": q}
    post_response = requests.post(url_post, json=newData)
    try:
        json =post_response.json()
        if not json:
            print("No result")
        else:
            id= json.get("id")
            name= json.get("namw")
            print("[{}] {}".format(id, name))
    except ValueError as e:
        print("Not a valid JSON")
    