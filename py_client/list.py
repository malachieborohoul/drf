import requests
from getpass import getpass
auth_endpoint="http://localhost:8000/api/auth/"
password=getpass()

auth_response = requests.post(auth_endpoint, json={"username":"bsm","password":password})

print(auth_response.json()) 


endpoint="http://localhost:8000/api/products/"


get_response = requests.get(endpoint)

print(get_response.json()) 

 