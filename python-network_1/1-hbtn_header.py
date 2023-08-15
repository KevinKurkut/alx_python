"""import  requests"""
import requests
"""Write a Python script that takes in a URL, sends a request to the URL and 
displays the value of the variable X-Request-Id in the response header"""
response = requests.get('https://alu-intranet.hbtn.io/status')
response.header.get('X-Request-Id')
