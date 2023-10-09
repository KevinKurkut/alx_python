import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter=sys.argv[1]
    else:
        letter=""
    param={'q':letter}
    url='http://0.0.0.0:5000/search_user'
    request=requests.post(url, data=param)    
    if request.headers.get('content-type'=='json'):
        if request.json()=={}:
            print("No result")
        else:
            id=request.json.get('id')
            name=request.json.get('name')
            print('[{}] {}'.format(id, name))
    else:
        print('Not a valid JSON')
        