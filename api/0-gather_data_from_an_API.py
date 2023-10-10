import requests
import sys
id=sys.argv[1]
request=requests.get('https://jsonplaceholder.typicode.com/users/'+id)
request2=requests.get('https://jsonplaceholder.typicode.com/users/'+id+'/todos')
data=request.json()
data2=request2.json()
completed=0
for i in data2:
    if i.get('completed')==True:
        completed=completed+1
print ('Employee {} is done with tasks({}/{}):'.format(data.get('name'), completed,len(data2)))
for item in data2:
    if item.get('completed')==True:
        print('\t '+item.get('title'))   
